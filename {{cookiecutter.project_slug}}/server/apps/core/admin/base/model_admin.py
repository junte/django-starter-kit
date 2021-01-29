from jnt_admin_tools.admin.base import BaseModelAdmin as LibBaseModelAdmin


class BaseModelAdmin(LibBaseModelAdmin):
    """Base model admin."""

    list_per_page = 20
