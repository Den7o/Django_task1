# Generated by Django 3.2.9 on 2021-11-30 12:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0004_auto_20211130_1850'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='data',
            name='year',
        ),
    ]
