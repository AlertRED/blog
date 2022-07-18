from django.db import models
from django.contrib.auth.models import User

from core.models import BasePost


class Tag(models.Model):
    title = models.CharField(
        max_length=32,
        null=False,
        unique=True,
        verbose_name='Название тега'
    )

    def __str__(self) -> str:
        return self.title


class Post(BasePost):
    tags = models.ManyToManyField(Tag)
