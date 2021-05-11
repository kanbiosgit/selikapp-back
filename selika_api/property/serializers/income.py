from property.models import Property, Comment
from rest_framework import serializers

class PropertyIncomeSerializer(serializers.ModelSerializer) :
  class Meta :
    model = Property
    fields = ['name', 'phone', 'address', 'price', 'ground', 'ref', 'prospecting', 'firstname', 'lastname', 'address', 'endDate']


class PropertySearchIncomeSerializer(serializers.ModelSerializer):
  class Meta:
    model = Property
    fields = ['name', 'phone', 'address']

class CommentIncomeSerializer(serializers.ModelSerializer):
  class Meta:
    model = Comment
    fields = ['text']
