# Generated by Django 4.1.5 on 2023-01-03 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('computer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computer',
            name='busy',
            field=models.BooleanField(default=False),
        ),
    ]
