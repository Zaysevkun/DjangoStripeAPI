from django.db import models


class Item(models.Model):
    name = models.CharField('Имя', max_length=255, default='')
    description = models.TextField('Описание', default='')
    price = models.CharField('Цена', max_length=30, default='')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Order(models.Model):
    Items = models.ManyToManyField(Item, verbose_name='Товары')


    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

