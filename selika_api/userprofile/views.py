from django.shortcuts import render
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, CreateAPIView
from rest_framework import status
from rest_framework.response import Response
from .models import UserProfile
from .serializers.income import UserProfileIncomeSerializer

# Create your views here.

class UserProfileView(RetrieveAPIView) :
  permission_classes = (IsAuthenticated,)
  
  def get(self, request):
    try :
      user = UserProfile.objects.get(user=request.user)
      print('user', user)
      statusCode = status.HTTP_200_OK
      response = {
        'sucess': True,
        'statusCode': statusCode,
        'message': 'User profile fetched successfully with id : ' + str(user.id),
      }

    except Exception as e:
      statusCode = status.HTTP_400_BAD_REQUEST
      response = {
          'success': False,
          'statusCode': statusCode,
          'message': 'User does not exists',
          'error': str(e)
          }
    return Response(response, status=statusCode)


class ListUserProfileAPIView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileIncomeSerializer


class GetUserProfileAPIView(RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileIncomeSerializer


class UpdateUserProfileAPIView(UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileIncomeSerializer


class DeleteUserProfileAPIView(DestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileIncomeSerializer


class CreateUserProfileAPIView(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileIncomeSerializer