from os import access
from rest_framework import serializers

from userprofile.models import UserProfile, UserCustomGroup



class UserLoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=128)
