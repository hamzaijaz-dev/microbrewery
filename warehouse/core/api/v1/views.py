import logging

from core.api.v1.serializers import ProductSerializer, RequestOrderSerializer
from core.models import Product
from core.producer import publish
from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

logger = logging.getLogger(__name__)


class ProductViewSet(GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @action(methods=['POST'], detail=True, url_path='place-order')
    def place_order(self, request, *args, **kwargs):
        try:
            product = self.get_object()
            serializer = RequestOrderSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)

            if product.remaining_quantity <= 0:
                return Response(data={'message': 'Product is out-of-stock.'}, status=400)

            elif request.data.get('order_quantity') <= product.remaining_quantity:
                price = product.sale_price if product.sale_price else product.price
                payload = {
                    'product_sku': product.sku,
                    'price': str(price),
                    'request_data': request.data
                }
                publish('product_available', payload)
                return Response(data={'message': 'Purchase request is initiated for this product.'}, status=200)

            else:
                return Response(
                    data={
                        'message': f'Only {product.remaining_quantity} items are available to sell in the warehouse.'
                    },
                    status=400
                )
        except Exception as e:
            logger.error(f"Error placing order: {str(e)}")
            return Response(
                data={'message': f'An error occurred while processing the order. reason: {str(e)}'},
                status=500
            )
