from property.models import Property
from rest_framework import serializers

class PropertyOutcomeSerializer(serializers.ModelSerializer) :
  class Meta :
    model = Property
    fields = ['name', 'phone', 'address', 'price', 'ground', 'comment', 'ref', 'prospecting', 'id']