from os import access
from rest_framework import serializers
from .models import AAUser
from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login
from rest_framework_simplejwt.tokens import RefreshToken
from userprofile.models import UserProfile, UserCustomGroup



class UserLoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=128, write_only=True)
    access = serializers.CharField(max_length=255, read_only=True)
    refresh = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        print('data', data)
        email = data.get("email", None)
        password = data.get("password", None)
        user = authenticate(email=email, password=password)
        if user is None:
          raise serializers.ValidationError(
              'A user with this email and password is not found.'
          )
        # profile_data = data.get("profile", None)
        # print('profile_data', profile_data)
        #
        # custom_group = UserCustomGroup.objects.create(
        #   label = profile_data['custom_group']['label']
        # )
        # if profile_data is not None :
        #     if UserProfile(user=user) is None :
        #       UserProfile.objects.create(
        #         user = user,
        #         firstname = profile_data['first_name'],
        #         lastname = profile_data['last_name'],
        #         custom_group = custom_group,
        #       )
        try:
            refresh = RefreshToken.for_user(user)
            update_last_login(None, user)
        except AAUser.DoesNotExist:
            raise serializers.ValidationError(
                'User with given email and password does not exists'
            )
        return {
            'email': email,
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }