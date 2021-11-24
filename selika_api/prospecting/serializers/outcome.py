from rest_framework import serializers
from ..models import Map, Negociator, Route


class MapOutcomeSerializer(serializers.ModelSerializer) :
    class Meta:
        model = Map
        fields = ['id', 'archived', 'creation']


class NegociatorOutcomeFromRouteSerializer(serializers.ModelSerializer) :
    class Meta:
        model = Negociator
        fields = ['color', 'lastname', 'firstname', 'id']


class RouteOutcomeSerializer(serializers.ModelSerializer):
    map = MapOutcomeSerializer(required=False)
    negociator = NegociatorOutcomeFromRouteSerializer(required=False)

    class Meta:
        model = Route
        fields = ['startLat', 'startLng', 'endLat', 'endLng', 'id', 'negociator', 'map', 'date']


class RouteOutcomeFromNegoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Route
        fields = ['startLat', 'startLng', 'endLat', 'endLng', 'id', 'negociator', 'date']


class NegociatorOutcomeSerializer(serializers.ModelSerializer):
    routes = RouteOutcomeFromNegoSerializer(many=True)

    class Meta:
        model = Negociator
        fields = ['color', 'lastname', 'firstname', 'id', 'routes']