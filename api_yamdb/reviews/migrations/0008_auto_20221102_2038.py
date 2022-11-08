# Generated by Django 2.2.16 on 2022-11-02 17:38

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0007_auto_20221102_2032'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='code',
        ),
        migrations.AddField(
            model_name='user',
            name='confirmation_code',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]
