from django.urls import include, path

urlpatterns = [
    path('api/v1/warehouse/', include('core.api.v1.urls')),
]
