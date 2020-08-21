# Generated by Django 3.0.7 on 2020-08-21 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20200820_1847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='internship',
            name='salary',
            field=models.CharField(choices=[('S0', 'Less than $500'), ('S1', 'Between $500 - $1000'), ('S2', 'Between $1000 - $1500'), ('S3', 'Between $1500 - $2000'), ('S4', 'Between $2000 - $2500'), ('S5', 'Between $2500 - $3000'), ('S6', 'Between $3000 - $4000'), ('S7', 'Between $4000 - $5000')], default=None, help_text='Enter as the complete amount for duration of working period.', max_length=1000, null=True, verbose_name='Salary'),
        ),
    ]