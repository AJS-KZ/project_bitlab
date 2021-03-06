from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf.urls import url


schema_view = get_schema_view(
   openapi.Info(
      title="PROJECT BITLAB API",
      default_version='V1',
      description="Some text of description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="a.jigitekov@gmail.com"),
      license=openapi.License(name="Project BITLAB License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


api_patterns = [
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path('drf-auth/', include('rest_framework.urls')),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('users/', include('users.urls')),
    path('questionnaires/', include('questionnaire.urls')),
    path('products/', include('products.urls')),
]


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(api_patterns))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
