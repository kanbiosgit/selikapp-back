from rest_framework import serializers
from ..models import AAUser
from userprofile.models import UserProfile

class UserOutcomeSerializer(serializers.ModelSerializer):
  

  class Meta:
    model = AAUser
    fields = ['email', 'id']
