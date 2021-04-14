from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from ..models import Route, Negociator, Map
from ..serializers.income import RouteIncomeSerializer
from ..serializers.outcome import RouteOutcomeSerializer
from rest_framework import status
from django.http import Http404


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