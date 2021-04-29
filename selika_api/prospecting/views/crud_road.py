from rest_framework.response import Response
from rest_framework.views import APIView
from ..models import Route, Negociator, Map
from ..serializers.income import RouteIncomeSerializer, RouteFromMapIncomeSerializer
from ..serializers.outcome import RouteOutcomeSerializer
from rest_framework import status
from django.http import Http404
from django.shortcuts import get_object_or_404



def get_route_from_map(pk, map):
    try:
        return Route.objects.get(id=pk, map=map)
    except Route.DoesNotExist:
        raise Http404
  
def get_map(pk):
    try:
        return Map.objects.get(pk=pk)
    except Map.DoesNotExist:
        raise Http404

class RouteFromMapList(APIView):
    """
    Api view for retrieve route from map
    """

    def get(self, request, pk, format=None):
      route = Route.objects.all().filter(map=get_map(pk))
      serializerOut = RouteOutcomeSerializer(route, many=True)
      return Response(serializerOut.data)


class RouteFromMapDetail(APIView):
    """
    Api view for retrieve route from map
    """

    def get(self, request, pk1, pk2, format=None):
      route = get_route_from_map(pk2, map=get_map(pk1))
      serializerOut = RouteOutcomeSerializer(route)
      return Response(serializerOut.data)


class RouteList(APIView):
    """
    List all routes, or create a new route.
    """
    def get(self, request, format=None):
        route = Route.objects.all()
        serializer = RouteOutcomeSerializer(route, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = RouteIncomeSerializer(data=request.data)
        negociator = Negociator.objects.get(user=request.user)
        if serializer.is_valid():
            route = serializer.save(negociator=negociator)
            serializerOut = RouteOutcomeSerializer(route)
            return Response(serializerOut.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RouteDetail(APIView):
    """
    Retrieve, update or delete a route instance.
    """
    def get_object(self, pk):
        try:
            return Route.objects.get(id=pk)
        except Route.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        route = self.get_object(pk)
        serializer = RouteIncomeSerializer(route)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        route = self.get_object(pk)
        serializer = RouteIncomeSerializer(route, data=request.data)
        negociator = Negociator.objects.get(user=request.user)
        if serializer.is_valid():
            route = serializer.save(negociator=negociator)
            serializerOut = RouteOutcomeSerializer(route)
            return Response(serializerOut.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        route = self.get_object(pk)
        route.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)