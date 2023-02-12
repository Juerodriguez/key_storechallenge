from rest_framework import serializers
from keys_storage_app.models import KeyModel, SharedEmail


class KeySerializers(serializers.ModelSerializer):
    class Meta:
        model = KeyModel
        fields = "__all__"
