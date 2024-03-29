from jnt_django_toolbox.admin.decorators import admin_field
from jnt_admin_tools.mixins import AutocompleteFieldsAdminMixin
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.contrib.auth.forms import AdminPasswordChangeForm
from django.urls import reverse
from django.utils.html import format_html

from apps.users.models import User


@admin.register(User)
class UserAdmin(
    AutocompleteFieldsAdminMixin,
    DjangoUserAdmin,
):
    """User admin."""

    list_display = (
        "login",
        "name",
        "email",
        "last_login",
        "is_active",
        "is_staff",
        "change_password_link",
    )
    list_filter = ("is_active", "is_staff", "is_active")
    ordering = ("login",)
    sortable_by = ()
    autocomplete_fields = ("groups",)
    search_fields = ("login",)
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("login", "password1", "password2"),
            },
        ),
    )

    exclude = ("user_permissions",)
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "login",
                    "email",
                    "name",
                    "is_superuser",
                    "is_staff",
                    "is_active",
                    "last_login",
                    "groups",
                ),
            },
        ),
    )
    readonly_fields = ("last_login",)
    change_password_form = AdminPasswordChangeForm

    @admin_field("Change password")
    def change_password_link(self, instance):
        """Change password link."""
        return format_html(
            '<a href="{0}">change password</a>',
            reverse(
                "admin:auth_user_password_change", kwargs={"id": instance.pk},
            ),
        )
