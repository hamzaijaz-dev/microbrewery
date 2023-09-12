from django.conf import settings
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.api.urls')),
]

if settings.DEBUG:
    from drf_yasg import openapi
    from drf_yasg.generators import OpenAPISchemaGenerator
    from drf_yasg.views import get_schema_view
    from rest_framework import permissions

    class SchemaGenerator(OpenAPISchemaGenerator):
        def get_schema(self, request=None, public=False):
            schema = super().get_schema(request, public)
            schema.schemes = ["http", "https"]
            return schema

    schema_view = get_schema_view(
        openapi.Info(
            title='Warehouse',
            default_version='v1',
        ),
        generator_class=SchemaGenerator,
        public=True,
        permission_classes=[permissions.AllowAny],
    )

    urlpatterns += [
        path('api/v1/docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    ]
