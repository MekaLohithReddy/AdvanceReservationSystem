# Generated by Django 3.0 on 2023-07-31 07:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_auto_20230731_1242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bus',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]