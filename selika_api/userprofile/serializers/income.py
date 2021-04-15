from rest_framework import serializers
from ..models import UserProfile, UserCustomGroup


class UserCustomGroupIncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCustomGroup
        fields = ['label']


class UserProfileIncomeSerializer(serializers.ModelSerializer):
    customGroup = UserCustomGroupIncomeSerializer(required=False)

    class Meta:
        model = UserProfile
        fields = ['lastname', 'firstname', 'customGroup']