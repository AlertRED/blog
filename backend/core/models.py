from django.db import models
from model_utils import Choices


class KeyValue(models.Model):
    TYPES = Choices(
        ('setting', 'Настройки сайта'),
        ('content', 'Часть контента'),
    )

    key = models.CharField(
        max_length=128,
        null=False,
        unique=True,
        verbose_name='Ключ'
    )
    value = models.CharField(
        max_length=65536,
        verbose_name='Значение'
    )
    type = models.CharField(
        choices=TYPES,
        null=False,
        max_length=32,
        verbose_name='Тип ключа'
    )

    def __str__(self) -> str:
        return super().__str__()


class TimeModel(models.Model):
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )
    updated = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата обновления'
    )

    def __str__(self) -> str:
        return super().__str__()


class BasePost(TimeModel):

    class Meta:
        ordering = ['-created']

    title = models.CharField(
        max_length=128,
        null=False,
        unique=True,
        verbose_name='Название поста'
    )
    body = models.CharField(
        max_length=65536,
        null=False,
        verbose_name='Содержание поста'
    )
    is_deleted = models.BooleanField(
        null=False,
        default=False,
        verbose_name='Объект удален'
    )
    is_draft = models.BooleanField(
        null=False,
        default=True,
        verbose_name='Черновик'
    )

    def __str__(self) -> str:
        return self.title
