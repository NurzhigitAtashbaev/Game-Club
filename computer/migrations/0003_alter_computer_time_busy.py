# Generated by Django 4.1.5 on 2023-01-05 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('computer', '0002_alter_computer_busy'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computer',
            name='time_busy',
            field=models.TimeField(),
        ),
    ]
