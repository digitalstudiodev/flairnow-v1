from django.db import models
from django.urls import reverse
from django.utils import timezone
from users.models import User, MAJORS, EDU_LEVEL, DEGREES, BINARY, GPA, US_STATES
from multiselectfield import MultiSelectField
from datetime import date
import calendar

def add_months(sourcedate, months):
    month = sourcedate.month - 1 + months
    year = sourcedate.year + month // 12
    month = month % 12 + 1
    day = min(sourcedate.day, calendar.monthrange(year,month)[1])
    return date(year, month, day)

TYPES = (
    ("IN","Internship"),
    ("SC","Scholarship"),
)

EXTERNAL_TYPES = (
    ("EIN","Internship"),
    ("ESC","Scholarship"),
)

CONFIRM = (
    ("Y","Yes, I Confirm"),
)

STATUS = (
    ("P","Pending"),
    ("A","Accepted"),
    ("D","Denied"),
    ("W","Wait List")
)

class Internship(models.Model):
    """
    -> internship model
    """
    organization = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=False)
    type = models.CharField(max_length=1000, choices=TYPES, default="IN", null=False, verbose_name="Opportunity Type")
    title = models.CharField(max_length=1000, default=None, null=False, verbose_name="Position Title")
    field = models.CharField(max_length=1000, choices=MAJORS, default=None, null=False)
    desc = models.TextField(verbose_name="Description", default=None, null=False)
    pos = models.IntegerField(default=1, null=False, verbose_name="# of Applicants")
    edu_level = models.CharField(max_length=1000, choices=EDU_LEVEL, default="None", null=False, verbose_name="Edu level")
    degree = models.CharField(max_length=1000, choices=DEGREES, default="None", null=False, verbose_name="Degree Type")
    gpa = models.CharField(max_length=1000, choices=GPA, verbose_name="GPA", default="None", null=False)
    salary = models.IntegerField(verbose_name="Amount", default=0, null=False, help_text="Enter as the complete amount for duration of working period.")
    valid_date = models.DateField(default=add_months(date.today(),3), verbose_name="Deadline")
    date_posted = models.DateField(default=date.today)
    city = models.CharField(max_length=1000, default=None, null=False, verbose_name="City")
    state = models.CharField(max_length=1000, choices=US_STATES, default=None, null=False, verbose_name="State")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('core:internship_detail', kwargs={'pk': self.pk})
    
    def get_apply_url(self):
        return reverse("core:internship_app_create", kwargs={'pk': self.pk})

class InternshipApp(models.Model):
    """
    -> internship application model
    -> functions as a connnection between the internship and the student
    """
    type = models.CharField(max_length=1000, choices=TYPES, default="IN", null=False, verbose_name="Application Type")
    internship = models.ForeignKey(Internship, on_delete=models.CASCADE, default=None, null=True)
    student = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=False)
    resume = models.FileField(default="sample_resume.pdf", upload_to='resumes', verbose_name="Resume", null=True)
    status = models.CharField(max_length=1000, choices=STATUS, default="P", null=True)
    confirm = MultiSelectField(choices=CONFIRM, max_length=1000, verbose_name="Are you sure? Plase Confirm.", unique=False, default=None)
    date_posted = models.DateField(default=date.today)

    def __str__(self):
        return self.student.email
    
    def get_absolute_url(self):
        return reverse('core:internship_app_detail', kwargs={'pk': self.id})

class Scholarship(models.Model):
    """
    -> scholarship model
    """
    organization = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=False)
    type = models.CharField(max_length=1000, choices=TYPES, default="SC", null=False, verbose_name="Opportunity Type")
    title = models.CharField(max_length=1000, default=None, null=False, verbose_name="Title")
    field = models.CharField(max_length=1000, choices=MAJORS, default=None, null=False)
    desc = models.TextField(verbose_name="Description", default=None, null=False)
    pos = models.IntegerField(default=1, null=False, verbose_name="# of Applicants")
    edu_level = models.CharField(max_length=1000, choices=EDU_LEVEL, default="None", null=False, verbose_name="Edu level")
    degree = models.CharField(max_length=1000, choices=DEGREES, default="None", null=False, verbose_name="Degree Type")
    gpa = models.CharField(max_length=1000, choices=GPA, verbose_name="GPA", default="None", null=False)
    salary = models.IntegerField(verbose_name="Amount", default=0, null=False, help_text="Enter as the complete amount.")
    valid_date = models.DateField(default=add_months(date.today(),3), verbose_name="Deadline")
    date_posted = models.DateField(default=date.today)
    city = models.CharField(max_length=1000, default=None, null=False, verbose_name="City")
    state = models.CharField(max_length=1000, choices=US_STATES, default=None, null=False, verbose_name="State")
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('core:scholarship_detail', kwargs={'pk': self.pk})
    
    def get_apply_url(self):
        return reverse("core:scholarship_app_create", kwargs={'pk': self.pk})

class ScholarshipApp(models.Model):
    """
    -> scholarship application model
    -> functions as a connnection between the scholarship and the student
    """
    type = models.CharField(max_length=1000, choices=TYPES, default="SC", null=True, verbose_name="Application Type")
    scholarship = models.ForeignKey(Scholarship, on_delete=models.CASCADE, default=None, null=True)
    student = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=False)
    resume = models.FileField(default="sample_resume.pdf", upload_to='resumes', verbose_name="Resume", null=True)
    status = models.CharField(max_length=1000, choices=STATUS, default="P", null=True)
    confirm = MultiSelectField(choices=CONFIRM, max_length=1000, verbose_name="Are you sure? Plase Confirm.", unique=False, default=None)
    date_posted = models.DateField(default=date.today)

    def __str__(self):
        return self.student.email
    
    def get_absolute_url(self):
        return reverse('core:scholarship_app_detail', kwargs={'pk': self.id})

class External(models.Model):
    """
    -> external opportunity model. 
    """
    organization = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=False)
    host = models.CharField(max_length=1000, verbose_name="Host", default=None, null=False)
    type = models.CharField(max_length=1000, choices=EXTERNAL_TYPES, default="SC", null=True, verbose_name="Opportunity Type")
    title = models.CharField(max_length=1000, default=None, null=True, verbose_name="Title")
    field = models.CharField(max_length=1000, choices=MAJORS, default=None, null=False)
    link = models.CharField(max_length=3000, verbose_name="Website Link", default="", null=True)
    date_posted = models.DateField(default=date.today)

    def __str__(self):
        return self.organization.email