# Generated by Django 3.0.7 on 2020-08-29 19:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0005_auto_20200829_1424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='internship',
            name='salary',
            field=models.CharField(choices=[('UP', 'Unpaid'), ('S0', 'Less than $500'), ('S1', 'Between $500 - $1000'), ('S2', 'Between $1000 - $1500'), ('S3', 'Between $1500 - $2000'), ('S4', 'Between $2000 - $2500'), ('S5', 'Between $2500 - $3000'), ('S6', 'Between $3000 - $4000'), ('S7', 'Between $4000 - $5000'), ('S8', 'Between $5000 - $6000'), ('S9', 'Between $6000 - $7000'), ('S10', 'Between $7000 - $8000'), ('S11', 'Between $8000 - $9000'), ('S12', 'Between $9000 - $10000'), ('S13', 'Over $10000')], default=None, help_text='Enter as the complete amount for duration of working period.', max_length=1000, null=True, verbose_name='Salary'),
        ),
        migrations.CreateModel(
            name='Scholarship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default=None, max_length=1000, null=True, verbose_name='Position Title')),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('field', models.CharField(choices=[('F0', 'Athletic Training'), ('F1', 'Biology'), ('F2', 'Chemistry'), ('F3', 'Phyics'), ('F4', 'Environmental Science'), ('F5', 'Exercise Sci/Kinesiology'), ('F6', 'Fisheries and Wildlife'), ('F7', 'Food Science'), ('F8', 'Forest Management'), ('F9', 'Marine Science'), ('F10', 'Nursing (RN/BSN)'), ('F11', 'Organic/Urban Farming'), ('F12', 'Pharmacy'), ('F13', 'Physicians Assistant'), ('F14', 'Pre - Dental'), ('F15', 'Pre - Medical'), ('F15', 'Pre - Veterinary Medicine'), ('L0', 'Apparel/Textile Design'), ('L1', 'Dance'), ('L2', 'Film/Broadcast'), ('L3', 'Fine/Studio Art'), ('L4', 'Graphic Design'), ('L5', 'Industrial Design'), ('L6', 'Interior Design'), ('L7', 'Landscape Architecture'), ('L8', 'Music'), ('L9', 'Theatre'), ('L10', 'Urban Planning'), ('L11', 'Video Game Design'), ('L12', 'Web Design/Digital Media'), ('A0', 'Arts Management'), ('A1', 'Education'), ('A2', 'Emergency Management'), ('A3', 'English/Writing'), ('A4', 'Equine Science/Mgmt'), ('A5', 'Family & Child Science'), ('A6', 'History'), ('A7', 'Journalism'), ('A8', 'Language Studies'), ('A9', 'Non-Profit Management'), ('A10', 'Parks and Recreation Management'), ('A11', 'Peace/Conflict Studies'), ('A12', 'Philosophy'), ('A13', 'Political Science'), ('A14', 'Psychology / Sociology'), ('A15', 'Sports Turf/Golf Mgmt'), ('A16', 'Women/Gender Studies'), ('I0', 'Aerospace Engineering'), ('I1', 'Astronomy / Physics'), ('I2', 'Aviation/Aeronautics'), ('I3', 'Biomedical Engineering'), ('I4', 'Chemical Engineering'), ('I5', 'Civil Engineering'), ('I6', 'Computer Science'), ('I7', 'Cyber Security'), ('I8', 'Electrical Engineering'), ('I9', 'Energy Science'), ('I10', 'Industrial Engineering'), ('I11', 'Industrial Technology'), ('I12', 'Materials Science'), ('I13', 'Mathematics'), ('I14', 'Mechanical Engineering'), ('R0', 'Accounting - General'), ('R1', 'Business - General'), ('R2', 'Construction Management'), ('R3', 'Data Science - Analytics'), ('R4', 'Economics (National + Global)'), ('R5', 'Finance'), ('R6', 'Hospitality Management'), ('R7', 'Human Resources Mgmt'), ('R8', 'Information Systems (MIS)'), ('R9', 'Insurance & Risk Mgmt'), ('R10', 'Marketing / Advertising'), ('R11', 'Public Health Administration'), ('R12', 'Sport Management'), ('R13', 'Supply Chain Mgmt (Logistics)')], default=None, max_length=1000, null=True)),
                ('description', models.TextField(default=None, null=True, verbose_name='Description')),
                ('number_of_appliants', models.IntegerField(default=None, null=True, verbose_name='Number of Applicants Seeking')),
                ('grade_level', models.CharField(choices=[('L0', 'Middle School (7, 8 Grades)'), ('L1', 'Grade 9 High School'), ('L2', 'Grade 10 High School'), ('L3', 'Grade 11 High School'), ('L4', 'Grade 12 High School'), ('L5', 'First Year Undergraduate'), ('L6', 'Second Year Undergraduate'), ('L7', 'Third Year Undergraduate'), ('L8', 'Fourth Year Undergraduate'), ('L9', 'Five Year or More Undergraduate'), ('L10', 'Graduate Student'), ('L11', 'Vocational Education'), ('P', 'Prefer Not To Say')], default=None, max_length=1000, null=True, verbose_name='This scholarship is intented for which grade level?')),
                ('degree', models.CharField(choices=[('L0', 'High School Diploma (or Equivalent)'), ('L1', 'Associate Degree'), ('L2', "Bachelor's Degree"), ('L3', "Master's Degree"), ('L4', 'Doctoral Degree'), ('P', 'Prefer Not To Say')], default=None, max_length=1000, null=True, verbose_name='What degree or level of knowledge is required?')),
                ('gpa', models.CharField(choices=[('N', "I don't have a GPA"), ('G0', 'Below 1.0'), ('G1', 'Between 1.0 and 1.5'), ('G2', 'Between 1.5 and 2.0'), ('G3', 'Between 2.0 and 2.5'), ('G4', 'Between 2.5 and 3.0'), ('G5', 'Between 3.0 and 3.5'), ('G6', 'Between 3.5 and 4.0'), ('P', 'Prefer Not To Say')], default=None, max_length=1000, null=True, verbose_name='GPA')),
                ('amount', models.CharField(choices=[('UP', 'Unpaid'), ('S0', 'Less than $500'), ('S1', 'Between $500 - $1000'), ('S2', 'Between $1000 - $1500'), ('S3', 'Between $1500 - $2000'), ('S4', 'Between $2000 - $2500'), ('S5', 'Between $2500 - $3000'), ('S6', 'Between $3000 - $4000'), ('S7', 'Between $4000 - $5000'), ('S8', 'Between $5000 - $6000'), ('S9', 'Between $6000 - $7000'), ('S10', 'Between $7000 - $8000'), ('S11', 'Between $8000 - $9000'), ('S12', 'Between $9000 - $10000'), ('S13', 'Over $10000')], default=None, help_text='Enter as the complete amount.', max_length=1000, null=True, verbose_name='Scholarship Amount')),
                ('organization', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]