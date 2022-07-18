from django.db import models


class TimeModel(models.Model):
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )
    updated = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата обновления'
    )


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
