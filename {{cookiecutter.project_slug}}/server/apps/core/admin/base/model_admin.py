# -*- coding: utf-8 -*-

from admin_tools.mixins import AdminAutocompleteFieldsMixin
from django.contrib import admin

from apps.core.admin.mixins import AdminFormFieldsOverridesMixin


class BaseModelAdmin(
    AdminAutocompleteFieldsMixin,
    AdminFormFieldsOverridesMixin,
    admin.ModelAdmin,
):
    """Base model admin."""

    list_per_page = 20

    class Media:
        """Media."""