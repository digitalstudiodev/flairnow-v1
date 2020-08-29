# Generated by Django 3.0.7 on 2020-08-29 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20200829_1602'),
    ]

    operations = [
        migrations.AddField(
            model_name='internship',
            name='type',
            field=models.CharField(choices=[('IN', 'Internship'), ('SC', 'Scholarship')], default='IN', max_length=1000, null=True, verbose_name='Opportunity Type'),
        ),
        migrations.AddField(
            model_name='scholarship',
            name='type',
            field=models.CharField(choices=[('IN', 'Internship'), ('SC', 'Scholarship')], default='SC', max_length=1000, null=True, verbose_name='Opportunity Type'),
        ),
    ]