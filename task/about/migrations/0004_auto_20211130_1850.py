# Generated by Django 3.2.9 on 2021-11-30 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0003_remove_data_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='year',
            field=models.PositiveSmallIntegerField(default=2019, null=True, verbose_name='Дата выхода'),
        ),
    ]
