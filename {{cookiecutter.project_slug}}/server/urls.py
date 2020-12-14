from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.utils.translation import gettext_lazy as _

admin.site.site_header = _("VN__ADMIN_DASHBOARD")
app_title = "{{cookiecutter.project_name}}"

urlpatterns = [
    path("ht/", include("health_check.urls")),
    path("admin_tools/", include("admin_tools.urls")),
    path("admin/", admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
