from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import KeySerializers, ShareSerializers
from .models import KeyModel, SharedEmail
from rest_framework import status
from .utils import encrypt, decrypt


class KeyAPIView(APIView):
    """
    View of all keys and create a new key.
    """
    def get(self, request: {str}, *args: any, **kwargs: any) -> Response:
        """
        List all keys.

        :param request:
        :param args:
        :param kwargs:
        :return: Json response
        """
        key_instance = KeyModel.objects.all()
        serializer = KeySerializers(key_instance, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request: {str}, *args, **kwargs) -> Response:
        """
        Create a new key.

        :param request:
        :param format:
        :return: Json response Success || Json response error
        """
        request.data["password"] = encrypt(request.data["password"])
        serializer = KeySerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class KeyDetailAPIView(APIView):
    """
    Detail of Keys, update and delete
    """

    def get(self, request: {str}, key_id: str, *args, **kwargs) -> Response:
        try:
            key_instance = KeyModel.objects.get(id=key_id)
            serializer = KeySerializers(key_instance)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except KeyModel.DoesNotExist:
            return Response(
                {"message": "Key does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

    def patch(self, request: {str}, key_id: str, *args, **kwargs) -> Response:
        try:
            key_instance = KeyModel.objects.get(id=key_id)
            data = {
                'name': request.data.get('name'),
                'password': encrypt(request.data.get('password'))
            }
            serializer = KeySerializers(instance=key_instance, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        except KeyModel.DoesNotExist:
            return Response(
                {"message": "Key does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

    def delete(self, request, key_id: str, *args, **kwargs) -> Response:
        try:
            key_instance = KeyModel.objects.get(id=key_id)
            key_instance.delete()
            return Response(status=status.HTTP_200_OK)
        except KeyModel.DoesNotExist:
            return Response(
                {"message": "Key does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )


class ShareAPIView(APIView):
    """
    View of all emails shared and post option.
    """
    def get(self, request: {str}, *args: any, **kwargs: any) -> Response:
        """
        List all emails shared.

        :param request:
        :param args:
        :param kwargs:
        :return: Json response
        """
        share_instance = SharedEmail.objects.all()
        serializer = ShareSerializers(share_instance, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, key_id, *args, **kwargs) -> Response:
        """
        Save a new email shared.

        :param request:
        :param key_id:
        :param format:
        :return: Json response Success || Json response error
        """
        key_instance = KeyModel.objects.get(id=key_id)
        serializer = ShareSerializers(data=request.data)

        if serializer.is_valid():
            serializer.save(key_related=key_instance)
            try:
                email_instance = SharedEmail.objects.filter(email=request.data["email"])
                send_mail(
                    subject=f"Password for {key_instance.name} key",
                    message=f"http://127.0.0.1:8000/api/v1/key_detail/decrypted/{key_id}/email_id/{email_instance[0].id}",
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[request.data["email"]]
                          )
            except BadHeaderError:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class KeyDetailDecryptedAPIView(APIView):
    """
    View of Key decrypted
    """
    def get(self, request: {str}, key_id: str, email_id: str, *args: any, **kwargs: any) -> Response:
        """
        View of Key decrypted.

        :param key_id:
        :param request:
        :param args:
        :param kwargs:
        :return: Json response
        """
        try:
            key_instance = KeyModel.objects.get(id=key_id)
            email_instance = SharedEmail.objects.get(id=email_id)
            client_ip = request.META.get('HTTP_X_FORWARDED_FOR', request.META.get('REMOTE_ADDR'))
            data = {
                "info_ip": client_ip,
                "visited": True
            }
            serializer = ShareSerializers(instance=email_instance, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
            key = decrypt(key_instance.password)
            return Response(key, status=status.HTTP_200_OK)
        except KeyModel.DoesNotExist:
            return Response(
                {"message": "Key does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
