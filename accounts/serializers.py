from django.contrib.auth.models import User
from rest_framework import serializers


class ReadOnlyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'is_active', 'last_login', 'is_superuser']


class WriteOnlyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password', 'is_active']

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        return user

#
# class CustomUserCreationForm(UserCreationForm):
#
#     class Meta(UserCreationForm):
#         model = User
#         fields = ('username', 'email')
#
# class CustomUserChangeForm(UserChangeForm):
#
#     class Meta:
#         model = User
#         fields = ('username', 'email')