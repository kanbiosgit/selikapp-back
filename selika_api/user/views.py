from user.models import AAUser
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .serializer import UserLoginSerializer
from rest_framework.generics import RetrieveAPIView
from django.contrib.auth import authenticate
from .models import AAUser
from django.contrib.auth.models import update_last_login
from rest_framework_simplejwt.tokens import RefreshToken


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
