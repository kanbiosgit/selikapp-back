from rest_framework.response import Response
from ..models import Negociator
from ..serializers.income import NegociatorIncomeSerializer, NegociatorIncomeColorSerializer, NegociatorCreateIncomeSerializer
from ..serializers.outcome import NegociatorOutcomeSerializer
from userprofile.models import UserCustomGroup, UserProfile
from user.models import AAUser
from rest_framework.views import APIView
from rest_framework import serializers, status
from django.http import Http404
from django.shortcuts import get_object_or_404
from property.models import Property



class NegociatorHimself(APIView):
    """
    in the other Negociator class you need to be an admin to modify a negociator, here the negociator modify it's own
    model
    """

    def get(self, request, format=None):
        negociator = get_object_or_404(Negociator, user=request.user)
        serializer = NegociatorOutcomeSerializer(negociator)
        return Response(serializer.data)

    def put(self, request, format=None):
        negociator = get_object_or_404(Negociator, user=request.user)
        serializer = NegociatorIncomeSerializer(negociator, data=request.data)
        if serializer.is_valid():
            negociator = serializer.save()
            serializerOut = NegociatorOutcomeSerializer(negociator)
            return Response(serializerOut.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class NegociatorList(APIView):
    """
    List all negociators, or create a new negociator.
    """
    def get(self, request, format=None):
        userprofile = UserProfile.objects.get(user=request.user)
        if userprofile.custom_group.label == 'Admin':
            negociator = Negociator.objects.exclude(firstname="DELETED")
            serializer = NegociatorOutcomeSerializer(negociator, many=True)
            return Response(serializer.data)
        try:
            negociator = Negociator.objects.get(user=request.user)
            serializer = NegociatorOutcomeSerializer(negociator)
            return Response(serializer.data)
        except Exception as e:
            response = {
                'success': False,
                'message': 'This user is nor an Admin or a negociator',
                'error': str(e)
            }
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, format=None):
        serializer = NegociatorCreateIncomeSerializer(data=request.data)
        if serializer.is_valid():
            negociator = serializer.save()
            serializerOut = NegociatorOutcomeSerializer(negociator)
            return Response(serializerOut.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NegociatorDetail(APIView):
    """
    Retrieve, update or delete a negociator instance.
    """
    def get_object(self, pk):
        try:
            return Negociator.objects.get(id=pk)
        except Negociator.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        userprofile = UserProfile.objects.get(user=request.user)
        if userprofile.custom_group.label == 'Admin':
            negociator = self.get_object(pk)
            serializer = NegociatorOutcomeSerializer(negociator)
            return Response(serializer.data)
        response = {
            'success': False,
            'message': 'You are not allowed'
        }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        userprofile = UserProfile.objects.get(user=request.user)
        if userprofile.custom_group.label == 'Admin':
            negociator = self.get_object(pk)
            serializer = NegociatorIncomeColorSerializer(negociator, data=request.data)
            if serializer.is_valid():
                negociator = serializer.save()
                serializerOut = NegociatorOutcomeSerializer(negociator)
                return Response(serializerOut.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        response = {
            'success': False,
            'message': 'Only admin can modify a negociator'
        }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        userprofile = UserProfile.objects.get(user=request.user)
        if userprofile.custom_group.label == 'Admin':
            negociator = self.get_object(pk)
            negociator.delete()
            negociators = Negociator.objects.exclude(firstname="DELETED")
            serializerOut = NegociatorOutcomeSerializer(negociators, many=True)
            return Response(data=serializerOut.data)
        response = {
            'success': False,
            'message': 'Only admin can modify a negociator'
        }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
