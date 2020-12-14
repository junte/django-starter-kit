from django.apps import AppConfig

from apps.core.utils.modules import load_module_from_app


class BaseAppConfig(AppConfig):
    """Base class representing a Django application and its configuration."""
