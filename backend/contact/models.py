from django.db import models
from core.models import BaseModel


class Contact(BaseModel):
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
