from django.db import models
from core.models import BasePost, BaseModel


class Category(BaseModel):
    title = models.CharField(
        max_length=32,
        null=False,
        unique=True,
        verbose_name='Название категории'
    )

    def __str__(self) -> str:
        return self.title


class Post(BasePost):
    category = models.ForeignKey(
        Category,
        related_name='posts',
        on_delete=models.PROTECT,
    )
