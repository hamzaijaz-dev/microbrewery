from core.models import Order
from rest_framework import serializers


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Order
        fields = '__all__'
