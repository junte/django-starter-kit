from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path
from django.utils.translation import gettext_lazy as _

{%- if cookiecutter.use_drf == "y" %}
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import authentication, permissions

from apps.core.utils.modules import get_module_url_patterns

{%- endif %}

admin.site.site_header = _('VN__ADMIN_DASHBOARD')

{%- if cookiecutter.use_drf == "y" %}

schema_view = get_schema_view(
    openapi.Info(
        title='{{cookiecutter.project_name}} API',
        default_version='v1',
        description='{{cookiecutter.project_name}} API',
    ),
    public=True,
    authentication_classes=(authentication.SessionAuthentication,),
    permission_classes=(permissions.IsAdminUser,),
)

{%- endif %}

urlpatterns = [
    path('ht/', include('health_check.urls')),

    {%- if cookiecutter.use_drf == "y" %}

    path('api/', include((get_module_url_patterns(
        'apps.users.rest.urls',
    ), 'urls'), namespace='api')),
    path('api/', include('apps.users.social_urls', namespace='social')),
    re_path(r'^api/swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='swagger-json'),
    path('api/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    {%- endif %}

    path('admin_tools/', include('admin_tools.urls')),
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
