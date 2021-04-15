from rest_framework import serializers
from ..models import UserProfile, UserCustomGroup


class UserCustomGroupOutcomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCustomGroup
        fields = ['label', 'id']


class UserProfileOutcomeSerializer(serializers.ModelSerializer):
    custom_group = UserCustomGroupOutcomeSerializer(required=False)

    class Meta:
        model = UserProfile
        fields = ['lastname', 'firstname', 'custom_group', 'id']