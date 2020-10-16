from django.db import models


class Item(models.Model):
    name = models.CharField('Имя', max_length=255, default='')
    description = models.TextField('Описание', default='')
    price = models.CharField('Цена', max_length=30, default='')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name


class Discount(models.Model):
    TYPE_CHOICES = [
        ('Процентная скидка', 'percentage'),
        ('Фиксированная скидка', 'fixed'),
    ]

    name = models.CharField('Название', max_length=255, default='')
    amount = models.CharField('Размер скидки', max_length=30, default='0')
    type = models.CharField('Тип скидки', max_length=32, choices=TYPE_CHOICES)

    class Meta:
        verbose_name = 'Скидка'
        verbose_name_plural = 'Скидки'

    def __str__(self):
        return self.name


class Tax(models.Model):
    name = models.CharField('Название', max_length=255, default='')
    amount = models.CharField('Процент налога', max_length=2, default='0')

    class Meta:
        verbose_name = 'Налог'
        verbose_name_plural = 'Налоги'

    def __str__(self):
        return self.name


class Order(models.Model):
    items = models.ManyToManyField(Item, verbose_name='Товары')
    discounts = models.ManyToManyField(Discount, blank=True, null=True)
    taxes = models.ManyToManyField(Tax, blank=True, null=True)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return self.name
