from property.models import Property, Comment
from rest_framework import serializers
from prospecting.serializers.outcome import NegociatorOutcomeSerializer



class PropertyOutcomeSerializer(serializers.ModelSerializer):
    negociator = NegociatorOutcomeSerializer(required=False)

    class Meta:
      model = Property
      fields = ['name', 'phone', 'address', 'price', 'ground', 'ref', 'prospecting', 'id', 'creation', 'negociator', 'firstname', 'lastname', 'email', 'endDate']

class CommentOutcomeSerializer(serializers.ModelSerializer):
  class Meta:
    model = Comment
    fields = ['text', 'creation', 'id']