from core.api.v1.serializers import RevenueSerializer
from core.models import Revenue
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet


class RevenueViewSet(GenericViewSet, mixins.ListModelMixin):
    queryset = Revenue.objects.all()
    serializer_class = RevenueSerializer
