from rest_framework import serializers
from ..models import Influencer

class InfluencerOutcomeSerializer(serializers.ModelSerializer) :
  class Meta: 
    model = Influencer
    fields = ['firstname', 'lastname', 'email', 'phone', 'lat', 'lng', 'comment', 'id']