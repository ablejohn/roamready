from rest_framework import serializers

class PlanATripSerializer(serializers.Serializer):
  prompt = serializers.CharField(required=True)