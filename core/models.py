from django.db import models
from django.urls import reverse
from django.utils import timezone
from users.models import User, MAJORS, CURRENT_GRADE_LEVEL, DEGREES, BINARY


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
)

STATUS = (
    ("P","Pending"),
    ("A","Accepted"),
    ("D","Denied"),
    ("W","Wait List")
)


class Internship(models.Model):
    organization = models.ForeignKey(User, on_delete=models.SET_NULL, default=None, null=True)
    ##basic information
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
    gpa = models.FloatField(verbose_name="GPA", default=None, null=True, help_text="Not Required")
    ##financial information
    salary = models.CharField(verbose_name="Salary", default=None, null=True, help_text="Enter as the complete amount for duration of working period.", max_length=1000, choices=SALARY)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('core:internship-detail', kwargs={'pk': self.pk})
    
    def get_apply_url(self):
        return reverse("core:apply-intern", kwargs={'pk': self.pk})

##Application
class InternshipApplication(models.Model):
    date_posted = models.DateTimeField(default=timezone.now)
    internship = models.ForeignKey(Internship, on_delete=models.SET_NULL, default=None, null=True)
    student = models.ForeignKey(User, on_delete=models.SET_NULL, default=None, null=True)
    status = models.CharField(max_length=1000, choices=STATUS, default="P", null=True)
    sure = models.CharField(max_length=1000, verbose_name="Are you sure?", choices=BINARY, default=None, null=True)

    def __str__(self):
        return str(self.date_posted)
    
    def get_absolute_url(self):
        return reverse('core:internship-detail', kwargs={'pk': self.internship.id})