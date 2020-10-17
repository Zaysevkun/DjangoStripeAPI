import uuid

from django.core.validators import MinValueValidator
from django.db import models


class Item(models.Model):
    name = models.CharField('Имя', max_length=255)
    description = models.TextField('Описание')
    price = models.FloatField('Цена', max_length=25, validators=[MinValueValidator(0.0)])

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name


class Discount(models.Model):
    class TypeChoices(models.TextChoices):
        PERCENTAGE = 'percentage', 'Процентная скидка'
        FIXED = 'fixed', 'Фиксированная скидка'

    name = models.CharField('Название', max_length=255)
    amount = models.FloatField('Размер скидки', max_length=25, validators=[MinValueValidator(0.0)])
    type = models.CharField('Тип скидки', max_length=32, choices=TypeChoices.choices,
                            default=TypeChoices.PERCENTAGE)

    class Meta:
        verbose_name = 'Скидка'
        verbose_name_plural = 'Скидки'

    def __str__(self):
        return self.name


class Tax(models.Model):
    name = models.CharField('Название', max_length=255)
    percentage = models.PositiveSmallIntegerField('Процент', default=13)

    class Meta:
        verbose_name = 'Налог'
        verbose_name_plural = 'Налоги'

    def __str__(self):
        return self.name


class Order(models.Model):
    class CurrencyChoices(models.TextChoices):
        USD = 'usd', 'Доллары'
        RUB = 'rub', 'Рубли'

    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    items = models.ManyToManyField(Item, verbose_name='Товары')
    currency = models.CharField('Валюта товара', max_length=10, choices=CurrencyChoices.choices,
                                default=CurrencyChoices.USD)
    discount = models.ForeignKey(Discount, models.SET_NULL,
                                 blank=True, null=True, verbose_name='Скидка')
    tax = models.ForeignKey(Tax, models.SET_NULL, blank=True,
                            null=True, verbose_name='Налог')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        default_related_name = 'orders'
