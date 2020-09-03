from django.db import models
from django.urls import reverse
from django.utils import timezone
from users.models import User, MAJORS, CURRENT_GRADE_LEVEL, DEGREES, BINARY, GPA
from multiselectfield import MultiSelectField

TYPES = (
    ("IN","Internship"),
    ("SC","Scholarship"),
)

CONFIRM = (
    ("Y","Yes, I Confirm"),
)

STATUS = (
    ("O","Open"),
    ("P","Pending"),
    ("C","Closed"),
)

SALARY = (
    ("UP","Unpaid"),
    ("S0","Less than $500"),
    ("S1","Between $500 - $1000"),
    ("S2","Between $1000 - $1500"),
    ("S3","Between $1500 - $2000"),
    ("S4","Between $2000 - $2500"),
    ("S5","Between $2500 - $3000"),
    ("S6","Between $3000 - $4000"),
    ("S7","Between $4000 - $5000"),
    ("S8","Between $5000 - $6000"),
    ("S9","Between $6000 - $7000"),
    ("S10","Between $7000 - $8000"),
    ("S11","Between $8000 - $9000"),
    ("S12","Between $9000 - $10000"),
    ("S13","Over $10000"),
)

STATUS = (
    ("P","Pending"),
    ("A","Accepted"),
    ("D","Denied"),
    ("W","Wait List")
)

##internship
"""
this is the internship model. 
"""
class Internship(models.Model):
    organization = models.ForeignKey(User, on_delete=models.SET_NULL, default=None, null=True)
    ##basic information
    type = models.CharField(max_length=1000, choices=TYPES, default="IN", null=True, verbose_name="Opportunity Type")
    title = models.CharField(max_length=1000, default=None, null=True, verbose_name="Position Title")
    date_posted = models.DateTimeField(default=timezone.now)
    industry = models.CharField(max_length=1000, choices=MAJORS, default=None, null=True)
    start_date = models.DateTimeField(verbose_name="Start Date", default=None, null=True)
    end_date = models.DateTimeField(verbose_name="End Date", default=None, null=True)
    description = models.TextField(verbose_name="Description", default=None, null=True)
    number_of_positions = models.IntegerField(default=None, null=True, verbose_name="Number of Available Positions")
    ##education requirements
    grade_level = models.CharField(max_length=1000, choices=CURRENT_GRADE_LEVEL, default=None, null=True, verbose_name="This internship is intented for which grade level?")
    degree = models.CharField(max_length=1000, choices=DEGREES, default=None, null=True, verbose_name="What degree or level of knowledge is required?")
    gpa = models.CharField(max_length=1000, choices=GPA, verbose_name="GPA", default=None, null=True)
    ##financial information
    salary = models.CharField(verbose_name="Salary", default=None, null=True, help_text="Enter as the complete amount for duration of working period.", max_length=1000, choices=SALARY)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('core:internship-detail', kwargs={'pk': self.pk})
    
    def get_apply_url(self):
        return reverse("core:apply-intern", kwargs={'pk': self.pk})

##internship application
"""
this is the internship application model. it functions as a connnection between the internship and the student
applying.
"""
class InternshipApplication(models.Model):
    date_posted = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=1000, choices=TYPES, default="IN", null=True, verbose_name="Application Type")
    internship = models.ForeignKey(Internship, on_delete=models.SET_NULL, default=None, null=True)
    student = models.ForeignKey(User, on_delete=models.SET_NULL, default=None, null=True)
    status = models.CharField(max_length=1000, choices=STATUS, default="P", null=True)
    confirm = MultiSelectField(choices=CONFIRM, max_length=1000, verbose_name="Are you sure? Plase Confirm.", unique=False, default=None)

    def __str__(self):
        return str(self.date_posted)
    
    def get_absolute_url(self):
        return reverse('core:internship-application-detail', kwargs={'pk': self.id})

##scholarship
"""
this is the scholarship model. 
"""
class Scholarship(models.Model):
    organization = models.ForeignKey(User, on_delete=models.SET_NULL, default=None, null=True)
    ##basic information
    type = models.CharField(max_length=1000, choices=TYPES, default="SC", null=True, verbose_name="Opportunity Type")
    title = models.CharField(max_length=1000, default=None, null=True, verbose_name="Position Title")
    date_posted = models.DateTimeField(default=timezone.now)
    field = models.CharField(max_length=1000, choices=MAJORS, default=None, null=True)
    description = models.TextField(verbose_name="Description", default=None, null=True)
    number_of_appliants = models.IntegerField(default=None, null=True, verbose_name="Number of Applicants Seeking")
    ##education requirements
    grade_level = models.CharField(max_length=1000, choices=CURRENT_GRADE_LEVEL, default=None, null=True, verbose_name="This scholarship is intented for which grade level?")
    degree = models.CharField(max_length=1000, choices=DEGREES, default=None, null=True, verbose_name="What degree or level of knowledge is required?")
    gpa = models.CharField(max_length=1000, choices=GPA, verbose_name="GPA", default=None, null=True)
    ##financial information
    amount = models.CharField(verbose_name="Scholarship Amount", default=None, null=True, help_text="Enter as the complete amount.", max_length=1000, choices=SALARY)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('core:scholarship-detail', kwargs={'pk': self.pk})
    
    def get_apply_url(self):
        return reverse("core:apply-scholarship", kwargs={'pk': self.pk})

##scholarship application
"""
this is the scholarship application model. it functions as a connnection between the internship and the student
applying.
"""
class ScholarshipApplication(models.Model):
    date_posted = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=1000, choices=TYPES, default="SC", null=True, verbose_name="Application Type")
    scholarship = models.ForeignKey(Scholarship, on_delete=models.SET_NULL, default=None, null=True)
    student = models.ForeignKey(User, on_delete=models.SET_NULL, default=None, null=True)
    status = models.CharField(max_length=1000, choices=STATUS, default="P", null=True)
    confirm = MultiSelectField(choices=CONFIRM, max_length=1000, verbose_name="Are you sure? Plase Confirm.", unique=False, default=None)

    def __str__(self):
        return str(self.date_posted)
    
    def get_absolute_url(self):
        return reverse('core:scholarship-detail', kwargs={'pk': self.scholarship.id})