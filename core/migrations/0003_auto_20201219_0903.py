# Generated by Django 3.0.7 on 2020-12-19 14:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20201218_1802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='internship',
            name='valid_date',
            field=models.DateField(default=datetime.date(2021, 3, 19), verbose_name='Deadline'),
        ),
        migrations.AlterField(
            model_name='scholarship',
            name='valid_date',
            field=models.DateField(default=datetime.date(2021, 3, 19), verbose_name='Deadline'),
        ),
    ]