# -*- coding: utf-8 -*-

INSTALLED_APPS = (
    "admin_tools",
    "admin_tools.theming",
    "admin_tools.menu",
    "admin_tools.dashboard",
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
    {%- if cookiecutter.use_drf == "y" %}
    "rest_framework",
    "corsheaders",
    {%- endif %}
    "admin_auto_filters",
    "health_check",
    "health_check.db",
    "health_check.cache",
    "health_check.storage",
    # apps
    "apps.core",
    "apps.users",
)
