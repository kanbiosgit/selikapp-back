from rest_framework import serializers
from ..models import Influencer

class InfluencerIncomeSerializer(serializers.ModelSerializer) :
  class Meta: 
    model = Influencer
    fields = ['firstname', 'lastname', 'email', 'phone', 'lat', 'lng', 'comment']
    extra_kwargs = {
      'firstname': {
        'allow_blank': True,
      },
      'lastname': {
        'allow_blank': True,
      },
      'email': {
        'allow_blank': True,
      },
      'phone': {
        'allow_blank': True,
      },
      'comment': {
        'allow_blank': True,
      },
    }