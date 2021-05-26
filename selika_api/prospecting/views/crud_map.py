from selika_api.responseHandler import respond
from rest_framework.response import Response
from ..models import Map
from ..serializers.income import MapIncomeSerializer
from ..serializers.outcome import MapOutcomeSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status


class LastMapDetail(APIView):
  def get(self, request, format=None):
    map = Map.objects.exclude(archived=True).last()
    if map is None :
      map = Map.objects.create(archived=False)
    serializer = MapOutcomeSerializer(map)
    return respond(status.HTTP_200_OK, serializer.data);

class MapList(APIView):
    """
    List all maps, or create a new map.
    """
    def get(self, request, format=None):
        maps = Map.objects.all()
        serializer = MapOutcomeSerializer(maps, many=True)
        return respond(status.HTTP_200_OK, serializer.data)

    def post(self, request, format=None):
        serializer = MapIncomeSerializer(data=request.data)
        if serializer.is_valid():
            map = serializer.save()
            serializerOut = MapOutcomeSerializer(map)
            return respond(data=serializerOut.data, response_status=status.HTTP_201_CREATED)
        return respond(error=serializer.errors, response_status=status.HTTP_400_BAD_REQUEST)


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
        return respond(status.HTTP_200_OK, serializer.data)

    def put(self, request, pk, format=None):
        map = self.get_object(pk)
        serializer = MapIncomeSerializer(map, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return respond(status.HTTP_200_OK, serializer.data)
        return respond(error=serializer.errors, response_status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        map = self.get_object(pk)
        map.delete()
        return respond(response_status=status.HTTP_204_NO_CONTENT)