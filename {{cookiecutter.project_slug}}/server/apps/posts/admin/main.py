from django.contrib import admin

from apps.core.admin.base import BaseModelAdmin
from ..models import Category, Post


@admin.register(Post)
class PostAdmin(BaseModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(BaseModelAdmin):
    pass
