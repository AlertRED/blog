from django.db import models
from core.models import TimeModel


class Contact(TimeModel):
    source_name = models.CharField(
        max_length=32,
        null=False,
        unique=True,
        verbose_name='Название ресурса'
    )
    contact_value = models.CharField(
        max_length=32,
        null=False,
        verbose_name='Значение контакта'
    )

    def __str__(self) -> str:
        return self.source_name, self.contact_value
