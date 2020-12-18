from jnt_admin_tools.mixins import AdminAutocompleteFieldsMixin
from django.contrib import admin


class BaseModelAdmin(
    AdminAutocompleteFieldsMixin,
    admin.ModelAdmin,
):
    """Base model admin."""

    list_per_page = 20

    class Media:
        """Media."""
