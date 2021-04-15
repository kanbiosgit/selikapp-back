from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from ..models import Map
from ..serializers.income import MapIncomeSerializer
from ..serializers.outcome import MapOutcomeSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class MapList(APIView):
    """
    List all maps, or create a new map.
    """
    def get(self, request, format=None):
        maps = Map.objects.all()
        serializer = MapOutcomeSerializer(maps, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MapIncomeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MapDetail(APIView):
    """
    Retrieve, update or delete a map instance.
    """
    def get_object(self, pk):
        try:
            return Map.objects.get(pk=pk)
        except Map.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        map = self.get_object(pk)
        serializer = MapOutcomeSerializer(map)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        map = self.get_object(pk)
        serializer = MapIncomeSerializer(map, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        map = self.get_object(pk)
        map.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)