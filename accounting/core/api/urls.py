from django.urls import include, path

urlpatterns = [
    path('api/v1/accounting/', include('core.api.v1.urls')),
]
