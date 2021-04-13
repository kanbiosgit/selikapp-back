from rest_framework import serializers
from ..models import Map, Negociator, Route


class MapOutcomeSerializer(serializers.ModelSerializer) :
    class Meta:
        model = Map
        fields = ['id', 'archived']


class RouteOutcomeSerializer(serializers.ModelSerializer) :
    class Meta:
        model = Route
        fields = ['startLat', 'startLng', 'endLat', 'endLng', 'id']


class NegociatorOutcomeSerializer(serializers.ModelSerializer) :
    class Meta:
        model = Negociator
        fields = ['color', 'user', 'lastname', 'firstname', 'id']