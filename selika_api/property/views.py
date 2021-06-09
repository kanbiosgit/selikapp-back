from selika_api.responseHandler import respond
from rest_framework import status
from .models import Property, Comment
from .serializers.income import PropertyIncomeSerializer, PropertySearchIncomeSerializer, CommentIncomeSerializer, PropertySearchIncomeNegociatorSerializer
from .serializers.outcome import PropertyOutcomeSerializer, CommentOutcomeSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from prospecting.models import Negociator
from userprofile.models import UserProfile
from django.db.models import Q
from datetime import date

# Create your views here.

def get_object(pk):
    try:
        return Property.objects.get(pk=pk)
    except Property.DoesNotExist:
        raise Http404

class CommentDetail(APIView):
  def delete(self, request, pk):
    comment = Comment.objects.get(pk=pk)
    comment.delete()
    return respond(response_status=status.HTTP_204_NO_CONTENT)

class CommentOnProperty(APIView):
  def get(self, request, pk):
    property = get_object(pk)
    comments = Comment.objects.all().filter(property=property)
    serializer = CommentOutcomeSerializer(comments, many=True)
    return respond(status.HTTP_200_OK, serializer.data)

  def post(self, request, pk) :
    serializer = CommentIncomeSerializer(data=request.data)
    if serializer.is_valid():
      property = get_object(pk)
      serializer.save(property=property)
      return respond(status.HTTP_200_OK, serializer.data)
    return respond(error=serializer.error_messages, response_status=status.HTTP_400_BAD_REQUEST)


class PropertyFromNegociator(APIView):
  def get(self, request):
    negociator = Negociator.objects.get(user=request.user)
    properties = Property.objects.all().filter(negociator=negociator)
    serializer = PropertyOutcomeSerializer(properties, many=True)
    return respond(status.HTTP_200_OK, serializer.data)


class PropertyFromAdmin(APIView):
  def get_object(self, id):
    try:
        return Negociator.objects.get(id=id)
    except Negociator.DoesNotExist:
        raise Http404

  def post(self, request, pk):
    negociator = self.get_object(pk)
    serializer = PropertyIncomeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(negociator=negociator, created_by_admin=True)
        return respond(data=serializer.data, response_status=status.HTTP_201_CREATED)
    return respond(error=serializer.errors, response_status=status.HTTP_400_BAD_REQUEST)
    

class PropertyListProspecting(APIView):

  def get(self, request) :
    properties = Property.objects.exclude(prospecting=False).exclude(endDate__lte=date.today())
    serializer = PropertyOutcomeSerializer(properties, many=True)
    return respond(status.HTTP_200_OK, serializer.data)

class PropertySearch(APIView):

    def get_object(self, id):
      try:
          return Negociator.objects.get(id=id)
      except Negociator.DoesNotExist:
          raise Http404
  
    def post(self, request):
        if request.user.userprofile.custom_group.label == 'Admin':
            properties = Property.objects.all()
        else:
            negociator = Negociator.objects.get(user=request.user)
            properties = Property.objects.filter(negociator=negociator)
        if 'email' in request.data:
            properties = properties.filter(email=request.data['email'])
        if 'phone' in request.data:
            properties = properties.filter(phone=request.data['phone'])
        if 'name' in request.data:
            properties = properties.filter(name__iexact=request.data['name'])
        if 'negociator' in request.data:
            properties = properties.filter(negociator=self.get_object(request.data['negociator']))
        if 'firstDate' in request.data:
            properties = properties.filter(creation__gte=request.data['firstDate'])
        if 'secondDate' in request.data:
            properties = properties.filter(creation__lte=request.data['secondDate'])
        if 'price' in request.data:
            properties = properties.filter(price__gte=request.data['price'][0]).filter(price__lte=request.data['price'][1])
        if 'ground' in request.data:
            properties = properties.filter(ground__gte=request.data['ground'][0]).filter(ground__lte=request.data['ground'][1])
        if 'created_by_admin' in request.data:
            properties = properties.filter(created_by_admin=True)
        return respond(status.HTTP_200_OK, data=PropertyOutcomeSerializer(properties, many=True).data)


class PropertyList(APIView):
    
    """
    List all propertys, or create a new property.
    """

    def get(self, request, format=None):
        properties = Property.objects.all()
        serializer = PropertyOutcomeSerializer(properties, many=True)
        return respond(status.HTTP_200_OK, serializer.data)

    def post(self, request, format=None):
        serializer = PropertyIncomeSerializer(data=request.data)
        if serializer.is_valid():
            negociator = get_object_or_404(Negociator, user=request.user)
            serializer.save(negociator=negociator)
            return respond(data=serializer.data, response_status=status.HTTP_201_CREATED)
        return respond(errors=serializer.errors, response_status=status.HTTP_400_BAD_REQUEST)


class PropertyDetail(APIView):
    
    """
    Retrieve, update or delete a property instance.
    """

    def get(self, request, pk, format=None):
        property = get_object(pk)
        serializer = PropertyOutcomeSerializer(property)
        return respond(status.HTTP_200_OK, serializer.data)

    def put(self, request, pk, format=None):
        property = get_object(pk)
        serializer = PropertyIncomeSerializer(property, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return respond(status.HTTP_200_OK, serializer.data)
        return respond(error=serializer.errors, response_status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        property = get_object(pk)
        property.delete()
        return respond(response_status=status.HTTP_204_NO_CONTENT)
