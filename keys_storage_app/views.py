from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import KeySerializers
from .models import KeyModel
from rest_framework import status


class KeyAPIView(APIView):
    """
    View of all keys and create a new key.
    """
    def get(self, request, *args, **kwargs):
        """
        List all keys.

        :param request:
        :param args:
        :param kwargs:
        :return: Json response
        """
        key = KeyModel.objects.all()
        serializer = KeySerializers(key, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        """
        Create a new key.

        :param request:
        :param format:
        :return: Json response Success || Json response error
        """
        serializer = KeySerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
