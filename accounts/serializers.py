"""Serializers create and read application user account."""
from rest_framework import serializers
from .models import User


class ReadOnlyUserSerializer(serializers.ModelSerializer):
    """Serialize of receiving user data."""

    class Meta:
        """Subclass for getting user model."""

        model = User
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'is_active',
            'last_login',
            'is_superuser',
        ]


class WriteOnlyUserSerializer(serializers.ModelSerializer):
    """Serialize of user creation and editing."""

    password = serializers.CharField(
        max_length=128,
        min_length=1,
        write_only=True,
    )
    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        """All fields that may be included in a request or response

         including fields password and token.

         """

        model = User
        fields = ['username', 'first_name', 'last_name', 'password', 'token']

    def create(self, validated_data):
        """User creation with method create_user."""
        return User.objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        """Update user data."""
        password = validated_data.pop('password', None)

        for key, value in validated_data.items():
            setattr(instance, key, value)

        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
