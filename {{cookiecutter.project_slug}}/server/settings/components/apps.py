INSTALLED_APPS = (
    "jnt_admin_tools",
    "jnt_admin_tools.theming",
    "jnt_admin_tools.menu",
    "jnt_admin_tools.dashboard",
    # Default django apps:
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # django-admin:
    "django.contrib.admin",
    "django.contrib.admindocs",
    # vendors
    "django_extensions",
    "django_filters",
    "rest_framework",
    {%- if cookiecutter.use_drf == "y" %}
    "corsheaders",
    {%- endif %}
    "health_check",
    "health_check.db",
    "health_check.cache",
    "health_check.storage",
    # apps
    "apps.core",
    "apps.users",
)
