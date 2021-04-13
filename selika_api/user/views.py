from userprofile.models import UserProfile
from user.models import AAUser
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .serializer import  UserLoginSerializer
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

class UserLoginView(RetrieveAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserLoginSerializer

    def post(self, request):
        print('request data', request.data)
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        response = {
            'success' : 'True',
            'status code' : status.HTTP_200_OK,
            'message': 'User logged in  successfully',
            'access_token' : serializer.data['access'],
            'refresh_token' : serializer.data['refresh'],
            }
        status_code = status.HTTP_200_OK

        return Response(response, status=status_code)





