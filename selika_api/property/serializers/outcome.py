from property.models import Property
from rest_framework import serializers
from prospecting.serializers.outcome import NegociatorOutcomeSerializer



class PropertyOutcomeSerializer(serializers.ModelSerializer):
    negociator = NegociatorOutcomeSerializer(required=False)

    class Meta:
      model = Property
      fields = ['name', 'phone', 'address', 'price', 'ground', 'comment', 'ref', 'prospecting', 'id', 'creation', 'negociator']
