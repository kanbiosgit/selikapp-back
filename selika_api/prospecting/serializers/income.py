from rest_framework import serializers
from ..models import Map, Negociator, Route


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

class RouteFromMapIncomeSerializer(serializers.ModelSerializer) :
    class Meta:
        model = Route
        fields = ['map']