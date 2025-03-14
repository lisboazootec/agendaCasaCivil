from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Configuração do Swagger para documentação da API
schema_view = get_schema_view(
   openapi.Info(
      title="Agendas API",
      default_version='v1',
      description="API para gerenciamento de agendas",
      contact=openapi.Contact(email="contato@exemplo.com"), # Change to your contact
      license=openapi.License(name="MIT License"), # Add a license
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('agenda.urls')),

    # URLs para documentação Swagger (Corrected Paths)
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]