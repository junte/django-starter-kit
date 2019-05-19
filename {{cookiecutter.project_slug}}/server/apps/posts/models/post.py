from django.db import models

from .category import Category


class Post(models.Model):
    title = models.CharField(
        max_length=255
    )

    content = models.TextField()

    category = models.ForeignKey(
        Category,
        models.CASCADE,
        related_name='posts'
    )

    def __str__(self):
        return self.title
