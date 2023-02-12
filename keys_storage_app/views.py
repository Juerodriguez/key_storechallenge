from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import KeySerializers
from .models import KeyModel
from rest_framework import status
from django.contrib.auth.hashers import make_password


class KeyAPIView(APIView):
    """
    View of all keys and create a new key.
    """
    def get(self, request, *args: any, **kwargs: any) -> Response:
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
        request.data["password"] = make_password(request.data["password"])
        serializer = KeySerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class KeyDetailAPIView(APIView):

    def get(self, request, key_id, *args, **kwargs) -> Response:
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
                'password': make_password(request.data.get('password'))
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


