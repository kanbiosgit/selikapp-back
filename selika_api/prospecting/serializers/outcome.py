from rest_framework import serializers
from ..models import Map, Negociator, Route


class MapOutcomeSerializer(serializers.ModelSerializer) :
    class Meta:
        model = Map
        fields = ['id', 'archived', 'creation']


class NegociatorOutcomeSerializer(serializers.ModelSerializer) :
    class Meta:
        model = Negociator
        fields = ['color', 'lastname', 'firstname', 'id']


class RouteOutcomeSerializer(serializers.ModelSerializer):
    map = MapOutcomeSerializer(required=False)
    negociator = NegociatorOutcomeSerializer(required=False)

    class Meta:
        model = Route
        fields = ['startLat', 'startLng', 'endLat', 'endLng', 'id', 'negociator', 'map']
