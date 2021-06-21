from django.http.response import Http404
from django.shortcuts import render
from rest_framework.views import APIView
from .serializers.income import InfluencerIncomeSerializer
from .serializers.outcome import InfluencerOutcomeSerializer
from selika_api.responseHandler import respond
from rest_framework import status
from .models import Influencer
# Create your views here.


class InfluencerList(APIView):
    
    """
    List all Influencers, or create a new Influencer.
    """

    def get(self, request, format=None):
        influencers = Influencer.objects.all()
        serializer = InfluencerOutcomeSerializer(influencers, many=True)
        return respond(status.HTTP_200_OK, serializer.data)

    def post(self, request, format=None):
        serializer = InfluencerIncomeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return respond(data=serializer.data, response_status=status.HTTP_201_CREATED)
        return respond(errors=serializer.errors, response_status=status.HTTP_400_BAD_REQUEST)

class InfluencerDetail(APIView):

  def get_object(pk):
    try:
        return Influencer.objects.get(pk=pk)
    except Influencer.DoesNotExist:
        raise Http404


  def get(self, request, pk, format=None) :
    influencer = self.get_object(pk)
    serializer = InfluencerOutcomeSerializer(influencer)
    return respond(data=serializer.data, response_status=status.HTTP_200_OK)