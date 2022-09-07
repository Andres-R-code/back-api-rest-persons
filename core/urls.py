from django.contrib import admin
from django.urls import path,include,re_path

from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from users.views import Login, Logout

schema_view = get_schema_view(
    openapi.Info(
        title="Documentación de API Persons",
        default_version='v0.1',
        description="Documentación pública de API prueba tecnica",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="andres.02rojas@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    path('logout/', Logout.as_view(), name = 'logout'),
    path('login/',Login.as_view(), name = 'login'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('users/',include('users.routers')),
    path('persons/',include('persons.routers')),
]
