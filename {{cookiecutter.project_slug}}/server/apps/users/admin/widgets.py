from typing import Any, Dict, List, Tuple

from django import forms
from django.conf import settings

DEFAULT_PERMISSIONS = ('add', 'change', 'delete', 'view')


class PermissionSelectMultipleWidget(forms.CheckboxSelectMultiple):
    template_name = 'users/widgets/permissions.html'
    custom_permission_types: List[str] = []
    groups_permissions: List[str] = []

    def get_context(self, name, value, attrs):
        if value is None:
            value = []

        return {
            'name': name,
            'value': value,
            'table': self.get_table(),
            'groups_permissions': self.groups_permissions,
            'default_permission_types': DEFAULT_PERMISSIONS,
            'custom_permission_types': self.custom_permission_types
        }

    def get_table(self):
        table = []
        row: Dict[str, Any] = {}

        for permission in self.choices.queryset.select_related('content_type').all():
            # if f'apps.{permission.content_type.app_label}' not in settings.PROJECT_APPS:
            #     continue

            row, created = self._update_or_create_permission_row(permission, row)
            if created:
                table.append(row)

        return table

    def _update_or_create_permission_row(self, permission, last_row: Dict[str, Any]) -> Tuple[Dict[str, Any], bool]:
        codename = permission.codename
        model_part = '_' + permission.content_type.model
        permission_type = codename
        if permission_type.endswith(model_part):
            permission_type = permission_type[:-len(model_part)]

        app = permission.content_type.app_label.replace('_', ' ')
        model_class = permission.content_type.model_class()
        model_verbose_name = model_class._meta.verbose_name if model_class else None

        if permission_type not in list(DEFAULT_PERMISSIONS) + self.custom_permission_types:
            self.custom_permission_types.append(permission_type)

        is_app_or_model_different = not last_row or (last_row['model_class'] != model_class or last_row['app'] != app)
        created = False

        if is_app_or_model_different:
            created = True
            row = dict(model=model_verbose_name,
                       model_class=model_class,
                       app=app,
                       permissions={})
        else:
            row = last_row

        row['permissions'][permission_type] = permission

        return row, created

    class Media:
        css = {
            'all': ('users/css/widgets/permissions.css',)
        }