# Generated by Django 3.0.7 on 2020-08-20 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='internship',
            name='degree',
            field=models.CharField(choices=[('L0', 'High School Diploma (or Equivalent)'), ('L1', 'Associate Degree'), ('L2', "Bachelor's Degree"), ('L3', "Master's Degree"), ('L4', 'Doctoral Degree')], default=None, max_length=1000, null=True, verbose_name='What degree or level of knowledge is required?'),
        ),
        migrations.AddField(
            model_name='internship',
            name='gpa',
            field=models.FloatField(default=None, help_text='Not Required', null=True, verbose_name='GPA'),
        ),
        migrations.AddField(
            model_name='internship',
            name='grade_level',
            field=models.CharField(choices=[('L0', 'Middle School (7, 8 Grades)'), ('L1', 'Grade 9 High School'), ('L2', 'Grade 10 High School'), ('L3', 'Grade 11 High School'), ('L4', 'Grade 12 High School'), ('L5', 'First Year Undergraduate'), ('L6', 'Second Year Undergraduate'), ('L7', 'Third Year Undergraduate'), ('L8', 'Fourth Year Undergraduate'), ('L9', 'Five Year or More Undergraduate'), ('L10', 'Graduate Student'), ('L11', 'Vocational Education')], default=None, max_length=1000, null=True, verbose_name='This internship is intented for which grade level?'),
        ),
        migrations.AddField(
            model_name='internship',
            name='paid',
            field=models.BooleanField(default=None, null=True, verbose_name='Is this intership paid?'),
        ),
        migrations.AddField(
            model_name='internship',
            name='salary',
            field=models.IntegerField(default=None, help_text='Enter as the complete amount for duration of working period.', null=True, verbose_name='Student Salary'),
        ),
    ]
