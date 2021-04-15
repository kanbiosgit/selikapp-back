from django.db.models import query
from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import ListAPIView, DestroyAPIView, UpdateAPIView, CreateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Property
from .serializers.income import PropertyIncomeSerializer, PropertySearchIncomeSerializer
from .serializers.outcome import PropertyOutcomeSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from prospecting.models import Negociator
from userprofile.models import UserProfile


# Create your views here.

class AdminPropertySearch(APIView):
    def get(self, request):
        serializer = PropertySearchIncomeSerializer(request.data)
        userprofile = UserProfile.objects.get(user=request.user)
        if userprofile.custom_group.label == 'Admin':
            properties = Property.objects.all().filter(phone=serializer.data['phone'],
                                                       address__iexact=serializer.data['address'], name__iexact=serializer.data['name'])
            serializerOut = PropertyOutcomeSerializer(properties)
            return Response(serializerOut.data)
        response = {
            'success': False,
            'message': 'Only admin can access this route'
        }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)


class PropertyList(APIView):
    """
    List all propertys, or create a new property.
    """

    def get(self, request, format=None):
        properties = Property.objects.all()
        serializer = PropertyOutcomeSerializer(properties, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PropertyIncomeSerializer(data=request.data)
        if serializer.is_valid():
            negociator = get_object_or_404(Negociator, user=request.user)
            serializer.save(negociator=negociator)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PropertyDetail(APIView):
    """
    Retrieve, update or delete a property instance.
    """

    def get_object(self, pk):
        try:
            return Property.objects.get(pk=pk)
        except Property.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        property = self.get_object(pk)
        serializer = PropertyOutcomeSerializer(property)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        property = self.get_object(pk)
        serializer = PropertyIncomeSerializer(property, data=request.data)
        if serializer.is_valid():
            negociator = get_object_or_404(Negociator, user=request.user)
            serializer.save(negociator=negociator)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        property = self.get_object(pk)
        property.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
