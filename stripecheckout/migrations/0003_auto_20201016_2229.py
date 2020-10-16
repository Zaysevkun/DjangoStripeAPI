# Generated by Django 3.1.2 on 2020-10-16 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stripecheckout', '0002_auto_20201016_2134'),
    ]

    operations = [
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255, verbose_name='Название')),
                ('amount', models.CharField(default='0', max_length=30, verbose_name='Размер скидки')),
                ('type', models.CharField(choices=[('Процентная скидка', 'percentage'), ('Фиксированная скидка', 'fixed')], max_length=32, verbose_name='Тип скидки')),
            ],
            options={
                'verbose_name': 'Скидка',
                'verbose_name_plural': 'Скидки',
            },
        ),
        migrations.CreateModel(
            name='Tax',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255, verbose_name='Название')),
                ('amount', models.CharField(default='0', max_length=2, verbose_name='Процент налога')),
            ],
            options={
                'verbose_name': 'Налог',
                'verbose_name_plural': 'Налоги',
            },
        ),
        migrations.AddField(
            model_name='order',
            name='discount',
            field=models.ManyToManyField(blank=True, null=True, to='stripecheckout.Discount'),
        ),
        migrations.AddField(
            model_name='order',
            name='tax',
            field=models.ManyToManyField(blank=True, null=True, to='stripecheckout.Tax'),
        ),
    ]
