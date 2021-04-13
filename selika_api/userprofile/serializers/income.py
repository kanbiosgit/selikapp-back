from rest_framework import serializers

class UserCustomGroupIncomeSerializer(serializers.Serializer):
  label = serializers.CharField(max_length=255)

class UserProfileIncomeSerializer(serializers.Serializer):
    firstname = serializers.CharField(max_length=255)
    lastname = serializers.CharField(max_length=255)
    customGroup = UserCustomGroupIncomeSerializer(required=False)