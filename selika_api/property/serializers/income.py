from property.models import Property, Comment
from rest_framework import serializers

class PropertyIncomeSerializer(serializers.ModelSerializer) :
  class Meta :
    model = Property
    fields = ['name', 'phone', 'price', 'ground', 'ref', 'prospecting', 'firstname', 'lastname', 'address', 'endDate', 'email', 'support', 'lat', 'lng']
    extra_kwargs = {
      'name': {
        'allow_blank': True,
      },
      'phone': {
        'allow_blank': True,
      },
      'ref': {
        'allow_blank': True,
      },
      'firstname': {
        'allow_blank': True,
      },
      'lastname': {
        'allow_blank': True,
      },
      'email': {
        'allow_blank': True,
      },
      'support': {
        'allow_blank': True,
      }
    }

class PropertySearchIncomeSerializer(serializers.Serializer):
    id = serializers.IntegerField(default=0)
    email = serializers.CharField(max_length=255, allow_blank=True)
    phone = serializers.CharField(max_length=255, allow_blank=True)
    name = serializers.CharField(max_length=255, allow_blank=True)

class PropertySearchIncomeNegociatorSerializer(serializers.ModelSerializer):
    class Meta:
      model = Property
      fields = ['name', 'phone', 'email']
      extra_kwargs = {
        'name': {
            'allow_blank': True,
          },
          'phone': {
            'allow_blank': True,
          },
          'email': {
            'allow_blank': True,
          }
      }

class CommentIncomeSerializer(serializers.ModelSerializer):
  class Meta:
    model = Comment
    fields = ['text']
