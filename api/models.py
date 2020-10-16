from django.db import models


class Item(models.Model):
    name = models.CharField('Имя', max_length=255, default='')
    description = models.TextField('Описание', default='')
    price = models.CharField('цена', max_length=30)

