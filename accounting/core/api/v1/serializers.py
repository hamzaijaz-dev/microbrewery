from core.models import Revenue
from rest_framework import serializers


class RevenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Revenue
        fields = '__all__'
