from core.api.v1.serializers import OrderSerializer
from core.models import Order
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet


class OrderViewSet(GenericViewSet, mixins.RetrieveModelMixin, mixins.ListModelMixin):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
