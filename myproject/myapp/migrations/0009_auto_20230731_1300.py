# Generated by Django 3.0 on 2023-07-31 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_auto_20230731_1253'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bus',
            options={'verbose_name_plural': 'List of Busses'},
        ),
        migrations.RemoveField(
            model_name='bus',
            name='date_option',
        ),
        migrations.AlterField(
            model_name='bus',
            name='date',
            field=models.DateField(),
        ),
    ]
