from os import access
from rest_framework import serializers


class UserLoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=128)

class UserRegistrationSerializer(serializers.Serializer):
  color = serializers.CharField(max_length=255)
  lastname = serializers.CharField(max_length=255)
  firstname = serializers.CharField(max_length=255)
  password = serializers.CharField(max_length=255)

class SendEmailSerializer(serializers.Serializer):
  email = serializers.CharField(max_length=255)