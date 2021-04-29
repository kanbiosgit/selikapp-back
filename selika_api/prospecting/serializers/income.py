from rest_framework import serializers
from ..models import Map, Negociator, Route
from user.models import AAUser
from userprofile.models import UserCustomGroup
from django.shortcuts import get_object_or_404


class MapIncomeSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Map
        fields = ['archived']


class RouteIncomeSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Route
        fields = ['map', 'startLat', 'startLng', 'endLat', 'endLng']


class NegociatorIncomeSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Negociator
        fields = ['color', 'lastname', 'firstname']

class NegociatorCreateIncomeSerializer(serializers.Serializer) :
    color = serializers.CharField(max_length=255)
    email = serializers.CharField(max_length=255)
    lastname = serializers.CharField(max_length=255)
    firstname = serializers.CharField(max_length=255)

    def create(self, validated_data):
      user = get_object_or_404(AAUser, email=validated_data['email'])
      userCust = UserCustomGroup.objects.create(label="Negociator")
      return Negociator.objects.create(user=user, custom_group=userCust, firstname=validated_data['firstname'],
                              lastname=validated_data['firstname'], color=validated_data['color'])


class NegociatorIncomeColorSerializer(serializers.ModelSerializer):
  class Meta:
    model = Negociator
    fields = ['color']

class RouteFromMapIncomeSerializer(serializers.ModelSerializer) :
    class Meta:
        model = Route
        fields = ['map']