
from core.api.v1.views import OrderViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('order-details', OrderViewSet, basename='product')
urlpatterns = router.urls
