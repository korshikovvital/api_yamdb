# Generated by Django 2.2.16 on 2022-11-11 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_auto_20221111_1122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='title',
            name='year',
            field=models.IntegerField(db_index=True, verbose_name='Год выхода'),
        ),
    ]