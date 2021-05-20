from .models import UserProfile
from .serializers.income import UserProfileIncomeSerializer
from .serializers.outcome import UserProfileOutcomeSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from selika_api.responseHandler import respond


class SelfUserProfile(APIView):
  def get(self, request):
    userprofile = UserProfile.get(user=request.user)
    serializer = UserProfileOutcomeSerializer(userprofile)
    return Response(serializer.data)


class UserProfileList(APIView):
    """
    List all userprofiles, or create a new userprofile.
    """
    def get(self, request, format=None):
        userprofiles = UserProfile.objects.all()
        serializer = UserProfileOutcomeSerializer(userprofiles, many=True)
        return respond(status.HTTP_200_OK, serializer.data)

    def post(self, request, format=None):
        serializer = UserProfileIncomeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return respond(serializer.data, response_status=status.HTTP_201_CREATED)
        return respond(error=serializer.errors, response_status=status.HTTP_400_BAD_REQUEST)


class UserProfileDetail(APIView):
    """
    Retrieve, update or delete a userprofile instance.
    """
    def get_object(self, pk):
        try:
            return request.user.userprofile(pk=pk)
        except UserProfile.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        userprofile = self.get_object(pk)
        serializer = UserProfileOutcomeSerializer(userprofile)
        return respond(status.HTTP_200_OK, serializer.data)

    def put(self, request, pk, format=None):
        userprofile = self.get_object(pk)
        serializer = UserProfileIncomeSerializer(userprofile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return respond(status.HTTP_200_OK, serializer.data)
        return respond(error=serializer.errors, response_status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        userprofile = self.get_object(pk)
        userprofile.delete()
        return respond(response_status=status.HTTP_204_NO_CONTENT)