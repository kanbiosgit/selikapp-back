from property.models import Property, Comment
from rest_framework import serializers

class PropertyIncomeSerializer(serializers.ModelSerializer) :
  class Meta :
    model = Property
    fields = ['name', 'phone', 'address', 'price', 'ground', 'ref', 'prospecting', 'firstname', 'lastname', 'address', 'endDate', 'email']


class PropertySearchIncomeSerializer(serializers.Serializer):
    id = serializers.IntegerField(default=0)
    email = serializers.EmailField()
    phone = serializers.CharField(max_length=255)
    name = serializers.CharField(max_length=255)

class CommentIncomeSerializer(serializers.ModelSerializer):
  class Meta:
    model = Comment
    fields = ['text']
