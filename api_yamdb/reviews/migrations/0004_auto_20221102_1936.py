# Generated by Django 2.2.16 on 2022-11-02 16:36

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_auto_20221102_1217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]