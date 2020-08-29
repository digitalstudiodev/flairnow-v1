# Generated by Django 3.0.7 on 2020-08-29 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='academic',
            name='act_score',
            field=models.CharField(choices=[('N', 'Did not take the ACT'), ('A0', 'Below 5'), ('A1', 'Between 5 and 7'), ('A2', 'Between 7 and 9'), ('A3', 'Between 9 and 11'), ('A4', 'Between 11 and 13'), ('A5', 'Between 13 and 15'), ('A6', 'Between 15 and 17'), ('A7', 'Between 17 and 19'), ('A8', 'Between 19 and 21'), ('A9', 'Between 21 and 23'), ('A10', 'Between 23 and 25'), ('A11', 'Between 25 and 27'), ('A12', 'Between 27 and 29'), ('A13', 'Between 29 and 31'), ('P', 'Prefer Not To Say')], default=None, max_length=1000, null=True, verbose_name='ACT Score'),
        ),
        migrations.AlterField(
            model_name='academic',
            name='current_grade_level',
            field=models.CharField(choices=[('L0', 'Middle School (7, 8 Grades)'), ('L1', 'Grade 9 High School'), ('L2', 'Grade 10 High School'), ('L3', 'Grade 11 High School'), ('L4', 'Grade 12 High School'), ('L5', 'First Year Undergraduate'), ('L6', 'Second Year Undergraduate'), ('L7', 'Third Year Undergraduate'), ('L8', 'Fourth Year Undergraduate'), ('L9', 'Five Year or More Undergraduate'), ('L10', 'Graduate Student'), ('L11', 'Vocational Education'), ('P', 'Prefer Not To Say')], default=None, max_length=1000, null=True, verbose_name='Current Grade Level'),
        ),
        migrations.AlterField(
            model_name='academic',
            name='degree_in_pursuit',
            field=models.CharField(choices=[('L0', 'High School Diploma (or Equivalent)'), ('L1', 'Associate Degree'), ('L2', "Bachelor's Degree"), ('L3', "Master's Degree"), ('L4', 'Doctoral Degree'), ('P', 'Prefer Not To Say')], default=None, max_length=1000, null=True, verbose_name='Degree You Are Currently Pursuing'),
        ),
        migrations.AlterField(
            model_name='academic',
            name='expected_grad_year',
            field=models.CharField(choices=[('1990', '1990'), ('1991', '1991'), ('1992', '1992'), ('1993', '1993'), ('1994', '1994'), ('1995', '1995'), ('1996', '1996'), ('1997', '1997'), ('1998', '1998'), ('1999', '1999'), ('2000', '2000'), ('2001', '2001'), ('2002', '2002'), ('2003', '2003'), ('2004', '2004'), ('2005', '2005'), ('2006', '2006'), ('2007', '2007'), ('2008', '2008'), ('2009', '2009'), ('2010', '2010'), ('2011', '2011'), ('2012', '2012'), ('2013', '2013'), ('2014', '2014'), ('2015', '2015'), ('2016', '2016'), ('2017', '2017'), ('2018', '2018'), ('2019', '2019'), ('2020', '2020'), ('2021', '2021'), ('2022', '2022'), ('2023', '2023'), ('2024', '2024'), ('2025', '2025'), ('2026', '2026'), ('2027', '2027'), ('2028', '2028'), ('2029', '2029'), ('2030', '2030'), ('2031', '2031'), ('2032', '2032'), ('2033', '2033'), ('2034', '2034'), ('2035', '2035'), ('2036', '2036'), ('2037', '2037'), ('2038', '2038'), ('2039', '2039'), ('2040', '2040'), ('P', 'Prefer Not To Say')], default=None, max_length=1000, null=True, verbose_name='Expected Graudation Year'),
        ),
        migrations.AlterField(
            model_name='academic',
            name='gpa',
            field=models.CharField(choices=[('N', "I don't have a GPA"), ('G0', 'Below 1.0'), ('G1', 'Between 1.0 and 1.5'), ('G2', 'Between 1.5 and 2.0'), ('G3', 'Between 2.0 and 2.5'), ('G4', 'Between 2.5 and 3.0'), ('G5', 'Between 3.0 and 3.5'), ('G6', 'Between 3.5 and 4.0'), ('P', 'Prefer Not To Say')], default=None, max_length=1000, null=True, verbose_name='GPA'),
        ),
        migrations.AlterField(
            model_name='academic',
            name='sat_score',
            field=models.CharField(choices=[('N', 'Did not take the SAT'), ('S0', 'Below 500'), ('S1', 'Between 500 and 550'), ('S2', 'Between 550 and 600'), ('S3', 'Between 600 and 650'), ('S4', 'Between 650 and 700'), ('S5', 'Between 700 and 750'), ('S6', 'Between 750 and 800'), ('S7', 'Between 800 and 850'), ('S8', 'Between 850 and 900'), ('S9', 'Between 900 and 950'), ('S10', 'Between 950 and 1000'), ('S11', 'Between 1000 and 1050'), ('S12', 'Between 1050 and 1100'), ('S13', 'Between 1100 and 1150'), ('S14', 'Between 1150 and 1200'), ('S15', 'Between 1200 and 1250'), ('S16', 'Between 1250 and 1300'), ('S17', 'Between 1300 and 1350'), ('S18', 'Between 1350 and 1400'), ('S19', 'Between 1400 and 1450'), ('S20', 'Between 1450 and 1500'), ('S21', 'Between 1500 and 1550'), ('S22', 'Between 1550 and 1600'), ('P', 'Prefer Not To Say')], default=None, max_length=1000, null=True, verbose_name='SAT Score'),
        ),
        migrations.AlterField(
            model_name='background',
            name='first_gen',
            field=models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default=None, max_length=1000, null=True, verbose_name='Are you the first in your family to go to college?'),
        ),
        migrations.AlterField(
            model_name='background',
            name='household_income',
            field=models.CharField(choices=[('HI0', 'Less than $10,000'), ('HI1', 'Between $10,000 - $25,000'), ('HI2', 'Between $25,000 - $50,000'), ('HI3', 'Between $50,000 - $100,000'), ('HI4', 'Between $100,000 - $150,000'), ('HI5', 'Between $150,000 - $200,000'), ('HI6', 'Over $200,000'), ('P', 'Prefer Not To Say')], default=None, max_length=1000, null=True, verbose_name='Household Income'),
        ),
        migrations.AlterField(
            model_name='background',
            name='household_size',
            field=models.CharField(choices=[('HS0', 'Small (Less than 3)'), ('HS1', 'Midsize (3-5)'), ('HS2', 'Large (Over 5)'), ('HS3', 'X-Large (Over 10)'), ('P', 'Prefer Not To Say')], default=None, max_length=1000, null=True, verbose_name='Household Size'),
        ),
        migrations.AlterField(
            model_name='background',
            name='race',
            field=models.CharField(choices=[('R0', 'American Indian or Alaska Native'), ('R1', 'Asian'), ('R2', 'Black or African American'), ('R3', 'Hispanic or Latino'), ('R4', 'Native Hawaiian or Other Pacific Islander'), ('R5', 'White'), ('P', 'Prefer Not To Say')], default=None, max_length=1000, null=True, verbose_name='Race'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='city',
            field=models.CharField(default='', max_length=1000, null=True, verbose_name='City'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='date_of_birth',
            field=models.CharField(default='', help_text='Please enter in the following format: MM/DD/YYY or MM-DD-YYY', max_length=10, null=True, verbose_name='Date of Birth'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone_number',
            field=models.CharField(default='', help_text='Please enter in the following format: 9734568456, with no spaces or special characters.', max_length=10, null=True, verbose_name='Phone Number'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='primary_address',
            field=models.CharField(default='', max_length=1000, null=True, verbose_name='Primary Address'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='zip_code',
            field=models.CharField(default='', max_length=1000, null=True, verbose_name='Zip Code'),
        ),
        migrations.AlterField(
            model_name='organizationcontact',
            name='facebook_link',
            field=models.CharField(default='', max_length=1000, null=True, verbose_name='Facebook Link'),
        ),
        migrations.AlterField(
            model_name='organizationcontact',
            name='linkedin_link',
            field=models.CharField(default='', max_length=1000, null=True, verbose_name='LinkedIn Link'),
        ),
        migrations.AlterField(
            model_name='organizationcontact',
            name='phone_number',
            field=models.CharField(default='', help_text='Please enter in the following format: 9734568456', max_length=10, null=True, verbose_name='Phone Number'),
        ),
        migrations.AlterField(
            model_name='organizationcontact',
            name='primary_address',
            field=models.CharField(default='', max_length=1000, null=True, verbose_name='Primary Address'),
        ),
        migrations.AlterField(
            model_name='organizationcontact',
            name='twitter_link',
            field=models.CharField(default='', max_length=1000, null=True, verbose_name='Twitter Link'),
        ),
        migrations.AlterField(
            model_name='organizationcontact',
            name='website_link',
            field=models.CharField(default='', max_length=1000, null=True, verbose_name='Website Link'),
        ),
        migrations.AlterField(
            model_name='organizationcontact',
            name='zip_code',
            field=models.CharField(default='', max_length=1000, null=True, verbose_name='Zip Code'),
        ),
    ]
