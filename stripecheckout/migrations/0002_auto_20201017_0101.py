# Generated by Django 3.1.2 on 2020-10-17 01:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stripecheckout', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='discounts',
            new_name='discount',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='taxes',
            new_name='tax',
        ),
    ]
