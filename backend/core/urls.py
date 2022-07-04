from django.contrib import admin
from django.urls import path, include
from users import views

from django.conf import settings
from django.conf.urls.static import static

from rest_framework.authtoken import views
from rest_framework import permissions
from drf_yasg.views import get_schema_view # new
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
    title="Blog API",
    default_version='v1',
    description="A sample API for learning DRF",
    terms_of_service="https://www.google.com/policies/terms/",
    contact=openapi.Contact(email="hello@example.com"),
    license=openapi.License(name="BSD License"),
    ),
public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('posts.urls')),
    path('swagger/', schema_view.with_ui(
    'swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui(
    'redoc', cache_timeout=0), name='schema-redoc'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('',include('users.urls')),
    path('api-token-auth', views.obtain_auth_token)
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)