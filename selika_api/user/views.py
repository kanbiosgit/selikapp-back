from django.conf import settings
from django.core.mail.message import EmailMultiAlternatives
from rest_framework.views import APIView
from user.models import AAUser
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .serializers.income import UserLoginSerializer, UserRegistrationSerializer, SendEmailSerializer
from .serializers.outcome import UserOutcomeSerializer
from rest_framework.generics import RetrieveAPIView
from django.contrib.auth import authenticate
from .models import AAUser
from django.contrib.auth.models import update_last_login
from rest_framework_simplejwt.tokens import RefreshToken
from userprofile.models import UserProfile
from userprofile.serializers.outcome import UserProfileOutcomeSerializer
from django.core.mail import send_mail
from django.template.loader import render_to_string
from userprofile.models import UserCustomGroup
from prospecting.models import Negociator


class UserLoginView(RetrieveAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserLoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.data['email']
        password = serializer.data['password']
        user = authenticate(email=email, password=password)
        if user is None:
            response = {
                'success': False,
                'status code': status.HTTP_400_BAD_REQUEST,
                'message': 'user not found'
            }
        else:
            try:
                refresh = RefreshToken.for_user(user)
                update_last_login(None, user)
            except AAUser.DoesNotExist:
                response = {
                    'success': False,
                    'status code': status.HTTP_400_BAD_REQUEST,
                    'message': 'User with given email and password does not exists'
                }
                return Response(response, status=status.HTTP_400_BAD_REQUEST)
            response = {
                'success': 'True',
                'status code': status.HTTP_200_OK,
                'message': 'User logged in  successfully',
                'access_token': str(refresh.access_token),
                'refresh_token': str(refresh),
            }
        status_code = status.HTTP_200_OK

        return Response(response, status=status_code)

class RetrieveUser(APIView):
    def get(self, request):
      userprofile = UserProfile.objects.get(user=request.user)
      serializer = UserProfileOutcomeSerializer(userprofile)
      return Response(serializer.data)

class createNegociator(APIView):
  permission_classes = (AllowAny,)

  def post(self, request, token):
    serializer = UserRegistrationSerializer(data=request.data)
    if serializer.is_valid():
      try:
        user = AAUser.objects.get(token=token)
        user.set_password(serializer.data['password'])
        user.first_connexion = False
        user.is_active = True
        user.is_admin = True
        userCust = UserCustomGroup.objects.create(label="Negociator")
        Negociator.objects.create(user=user, custom_group=userCust, firstname=serializer.data['firstname'],
                              lastname=serializer.data['lastname'], color=serializer.data['color'])
        user.save()
        response = {
          'success': True,
          'message': 'Negociator create'
        }
        return Response(response, status=status.HTTP_200_OK)
      except:
        response = {
          'success': False,
          'message': 'User not found, token is expired'
        }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
    response = {
      'success': False,
      'message': 'bad request'
    }
    return Response(response, status=status.HTTP_400_BAD_REQUEST)

class sendEmail(APIView):
  def post(self, request):
    serializer = SendEmailSerializer(data=request.data)
    if serializer.is_valid():
      try:
        user = AAUser.objects.create(email=serializer.data['email'])
        user.save()
      except:
        response = {
          'success': False,
          'message': 'User already exist'
        }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
      else:
        print('user token', user.token)
        msg_plain = render_to_string(
          'negociator-invitation.html',
          {'link': 'http://localhost:8080/' + 'creation/negociator/' + user.token},
        )
        msg = EmailMultiAlternatives(
          'Selika app : Création de négociateur',
          msg_plain,
          settings.DEFAULT_FROM_EMAIL,
          [user.email]
        )
        msg.send()
        response = {
          'success': True,
        }
        return Response(response, status=status.HTTP_200_OK)
    response = {
      'success': False,
      'message': 'bad argument'
    }
    return Response(response, status=status.HTTP_400_BAD_REQUEST)