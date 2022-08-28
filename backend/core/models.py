import uuid
from django.db import models
from django.utils import timezone
from model_utils import Choices


class TimeStampModel(models.Model):

    class Meta:
        abstract = True

    created = models.DateTimeField(
        editable=False,
        db_index=True,
        verbose_name='Дата создания',
        default=timezone.now,
    )
    updated = models.DateTimeField(
        editable=False,
        db_index=True,
        verbose_name='Дата обновления',
        default=timezone.now,
    )

    def __str__(self) -> str:
        return super().__str__()


class UUIDPKModel(models.Model):
    """ Абстрактный класс с идентификатором UUID
    """

    class Meta:
        abstract = True

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid1,
        editable=False,
    )


class BaseModel(UUIDPKModel, TimeStampModel):
    """ Базовый класс сущности
    """

    class Meta:
        abstract = True


class KeyValue(BaseModel):
    TYPES = Choices(
        ('setting', 'Настройки сайта'),
        ('content', 'Часть контента'),
    )

    key = models.CharField(
        max_length=128,
        null=False,
        unique=True,
        verbose_name='Ключ',
    )
    value = models.CharField(
        max_length=65536,
        verbose_name='Значение',
    )
    type = models.CharField(
        choices=TYPES,
        null=False,
        max_length=32,
        verbose_name='Тип ключа',
    )

    def __str__(self) -> str:
        return super().__str__()


class BasePost(BaseModel):

    class Meta:
        abstract = True
        ordering = ['-created']

    title = models.CharField(
        max_length=128,
        unique=True,
        verbose_name='Название поста',
    )
    body = models.CharField(
        max_length=65536,
        verbose_name='Содержание поста',
    )
    is_deleted = models.BooleanField(
        null=False,
        default=False,
        verbose_name='Объект удален',
    )
    is_draft = models.BooleanField(
        null=False,
        default=True,
        verbose_name='Черновик',
    )

    def __str__(self) -> str:
        return self.title
