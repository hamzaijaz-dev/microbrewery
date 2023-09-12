from core.models import Product
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        depth = 1
        model = Product
        fields = '__all__'


class RequestOrderSerializer(serializers.Serializer):
    name = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    phone_number = serializers.IntegerField(required=True)
    address = serializers.CharField(required=True)
    city = serializers.CharField(required=True)
    zip_code = serializers.CharField(required=True)
    order_quantity = serializers.IntegerField(required=True)
