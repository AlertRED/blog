from django.db import models
from core.models import BasePost, TimeModel


class Tag(TimeModel):
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
