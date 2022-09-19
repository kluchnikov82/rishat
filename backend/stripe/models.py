from django.db import models
import uuid


class Item(models.Model):
    """
        Модель Задачи
    """
    uuid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)

    name = models.CharField(
        max_length=255,
        blank=False,
        verbose_name='Наименование'
    )

    description = models.CharField(
        max_length=255,
        blank=False,
        verbose_name='Описание'
    )

    price = models.IntegerField(
        default=0,
        verbose_name='Цена')

    created = models.DateTimeField(auto_now_add=True,
                                   verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now=True,
                                   verbose_name='Дата последнего изменения')
    deleted = models.DateTimeField(null=True,
                                   default=None,
                                   verbose_name='Дата удаления')


    class Meta:
        verbose_name = 'Элемент полосы сессии'
        verbose_name_plural = 'Элементы полосы сессии'
        db_table = 'stripe'

