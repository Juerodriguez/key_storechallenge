from rest_framework import serializers
from keys_storage_app.models import KeyModel, SharedEmail


class ShareSerializers(serializers.ModelSerializer):
    class Meta:
        model = SharedEmail
        fields = "__all__"


class KeySerializers(serializers.ModelSerializer):
    shared_at = ShareSerializers(many=True, read_only=True)

    class Meta:
        model = KeyModel
        fields = "__all__"
