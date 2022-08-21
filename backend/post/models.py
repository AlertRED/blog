from django.db import models
import os

from core.models import (
    BasePost,
    BaseModel,
)


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


def post_file_name(instance, filename):
    """Функция для генерации наименования файла"""
    hex_pk = instance.pk.hex
    return f'posts/{hex_pk[:2]}/{filename}'


class PostFile(BaseModel):
    """Класс модели для файлов содержания поста"""
    class Meta:
        verbose_name = 'Файл содержания поста'
        verbose_name_plural = 'Файлы содержания поста'

    path = models.FileField(
        verbose_name='Путь к файлу',
        upload_to=post_file_name,
        blank=True,
        null=True,
    )

    @property
    def basename(self):
        """Имя файла"""
        return os.path.basename(self.path.name) if self.path else None
