# Generated by Django 4.1.5 on 2023-01-05 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('computer', '0003_alter_computer_time_busy'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='computer',
            name='time_busy',
        ),
        migrations.AddField(
            model_name='computer',
            name='busy_until',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
