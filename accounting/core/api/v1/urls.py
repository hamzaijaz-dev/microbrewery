
from core.api.v1.views import RevenueViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('revenue-details', RevenueViewSet, basename='revenue_details')
urlpatterns = router.urls
