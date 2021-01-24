# serializers.pyfrom rest_framework import serializers
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Song

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email")


# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email", "password")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data["username"],
            validated_data["email"],
            validated_data["password"],
        )

        return user


# Change password serializer
class ChangePasswordSerializer(serializers.Serializer):
    model = User

    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    new_password2 = serializers.CharField(required=True)


# Song Serializer
class SongSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Song
        fields = ("id", "title", "song", "voice", "melody")

    def create(self, validated_data):
        request = self.context.get("request")
        user_id = request.auth.payload.get("user_id")
        validated_data["user_id"] = user_id
        return super().create(validated_data)
