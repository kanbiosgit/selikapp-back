from rest_framework import serializers
from ..models import UserProfile, UserCustomGroup


class UserCustomGroupIncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCustomGroup
        fields = ['label']


class UserProfileIncomeSerializer(serializers.ModelSerializer):
    custom_group = UserCustomGroupIncomeSerializer(required=False)

    def create(self, validated_data):
        label = validated_data['custom_group']['label']
        customGroup = UserCustomGroup.objects.create(label=label)
        return UserProfile.objects.create(custom_group=customGroup,
                                          lastname=validated_data['lastname'], firstname=validated_data['firstname'],
                                          user=validated_data['user'])

    class Meta:
        model = UserProfile
        fields = ['lastname', 'firstname', 'custom_group']