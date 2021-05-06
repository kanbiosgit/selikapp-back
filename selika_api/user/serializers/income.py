from os import access
from rest_framework import serializers


class UserLoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=128)

class UserRegistrationSerializer(serializers.Serializer):
  email = serializers.CharField(max_length=255)
  password = serializers.CharField(max_length=255)
  confirmPassword = serializers.CharField(max_length=255)

class SendEmailSerializer(serializers.Serializer):
  email = serializers.CharField(max_length=255)