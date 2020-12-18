from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from PIL import Image
from django.urls import reverse
from django.utils import timezone
from multiselectfield import MultiSelectField
from datetime import date
from .dict_lib import (BINARY, YEARS, ORG_TYPES, US_STATES, HOUSE_INCOME, HOUSE_SIZE, CITIZENSHIP, RACE, SEX, GENDERS, EDU_LEVEL, DEGREES, MAJORS, WORK, VALUES, ENV, ACT, SKILLS)


class Manager(BaseUserManager):
    def create_user(self, first_name, last_name, org_name, email, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        if not first_name:
            raise ValueError("Users must have a first name")
        if not last_name:
            raise ValueError("Users must have a last name")
        if not org_name:
            raise ValueError("Users must have an organization name")

        user = self.model(
            first_name=first_name,
            last_name=last_name,
            org_name=org_name,
            email=self.normalize_email(email),
            password=password,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, first_name, last_name, org_name, email, password):
        user = self.create_user(
            first_name=first_name,
            last_name=last_name,
            org_name=org_name,
            email=self.normalize_email(email),
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(verbose_name="Email Address", max_length=60, unique=True)
    date_joined = models.DateTimeField(verbose_name="Date Joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="Last Login", auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    first_name = models.CharField(max_length=30, default=None, null=True, blank=True, verbose_name="First Name")
    last_name = models.CharField(max_length=30, default=None, null=True, blank=True, verbose_name="Last Name")
    org_name = models.CharField(max_length=30, default=None, null=True, blank=True, verbose_name="Organization Name")
    is_student = models.BooleanField(default=True)
    is_organization = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'org_name']

    objects = Manager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile_pics', verbose_name="Profile Picture")

    def __str__(self):
        return f'{self.user.email} Profile'

class Edu(models.Model):
    student = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Student")
    school = models.CharField(max_length=50, default=None, blank=True, verbose_name="Current or Preferred Institution")
    city = models.CharField(max_length=50, default=None, blank=True, verbose_name="City")
    state = models.CharField(max_length=1000, choices=US_STATES, default=None, blank=True, verbose_name="State")
    edu_level = models.CharField(max_length=1000, choices=EDU_LEVEL, default=None, blank=True, verbose_name="Edu Level")
    degree = models.CharField(max_length=1000, choices=DEGREES, default=None, blank=True, verbose_name="Degree You Are Currently Pursuing")
    major = MultiSelectField(max_length=1000, choices=MAJORS, max_choices=3, default=None, blank=True, verbose_name="Current Major or Field")
    con = MultiSelectField(max_length=1000, choices=MAJORS, verbose_name="Minor or Concentration", default=None, blank=True)
    grad_year = models.CharField(max_length=1000, choices=YEARS, default=None, blank=True, verbose_name="Grad Year")
    
    def __str__(self):
        return self.student.email

    def get_absolute_url(self):
        return reverse('users:edu_detail', kwargs={'pk': self.pk})

class Demo(models.Model):
    student = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Student")
    gender = models.CharField(max_length=1000, choices=GENDERS, default=None, blank=True, verbose_name="Gender")
    sex = models.CharField(max_length=1000, choices=SEX, default=None, blank=True, verbose_name="Sexual Orientation")
    race = models.CharField(max_length=1000, choices=RACE, default=None, blank=True, verbose_name="Race")
    cit = models.CharField(max_length=1000, choices=CITIZENSHIP, default=None, blank=True, verbose_name="Citizenship")
    house_size = models.CharField(max_length=1000, choices=HOUSE_SIZE, default=None, blank=True, verbose_name="Household Size")
    house_income = models.CharField(max_length=1000, choices=HOUSE_INCOME, default=None, blank=True, verbose_name="Household Income")
    first_gen = models.CharField(max_length=1000, choices=BINARY, default=None, blank=True, verbose_name="Are you the first in your family to go to college?")
    
    def __str__(self):
        return self.student.email

    def get_absolute_url(self):
        return reverse('users:demo_detail', kwargs={'pk': self.pk})

class Contact(models.Model):
    student = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Student")
    phone = models.CharField(default=None, blank=True, max_length=10, verbose_name="Phone Number")
    dob = models.DateField(default=timezone.now(), verbose_name="Date of Birth")
    street = models.CharField(max_length=50, default=None, blank=True, verbose_name="Primary Address", help_text="Ex 123 Main Street")
    apt = models.CharField(max_length=10, default=None, blank=True, verbose_name="Secondary Address", help_text="Ex Apt 13 W")
    zip_code = models.CharField(max_length=5, default=None, blank=True, verbose_name="Zip Code", help_text="Ex 07102")
    city = models.CharField(max_length=50, default=None, blank=True, verbose_name="City")
    state = models.CharField(max_length=1000, choices=US_STATES, default=None, blank=True, verbose_name="State")
    linkedin = models.CharField(max_length=150, default=None, blank=True, verbose_name="LinkedIn URL", help_text="Ex: https://www.linkedin.com/in/your-profile")
    
    def __str__(self):
        return self.student.email

    def get_absolute_url(self):
        return reverse('users:contact_detail', kwargs={'pk': self.pk})

class OrgContact(models.Model):
    org = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Organization")
    phone = models.CharField(max_length=10, default=None, blank=True, verbose_name="Phone Number")
    street = models.CharField(max_length=50, default=None, blank=True, verbose_name="Primary Address", help_text="Ex 123 Main Street")
    apt = models.CharField(max_length=10, default=None, blank=True, verbose_name="Secondary Address", help_text="Ex Apt 13 W")
    zip_code = models.CharField(max_length=5, default=None, blank=True, verbose_name="Zip Code", help_text="Example 07102")
    city = models.CharField(max_length=1000, default=None, blank=True, verbose_name="City")
    state = models.CharField(max_length=1000, choices=US_STATES, default=None, blank=True, verbose_name="State")
    website_link = models.CharField(max_length=1000, default=None, blank=True, verbose_name="Website Link")
    linkedin = models.CharField(max_length=150, default=None, blank=True, verbose_name="LinkedIn URL", help_text="Ex: https://www.linkedin.com/company/your-profile")

    def __str__(self):
        return self.org.email

    def get_absolute_url(self):
        return reverse('users:orgcontact_detail', kwargs={'pk': self.pk})

class OrgDemo(models.Model):
    org = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Organization")
    size = models.IntegerField(default=1, blank=True, verbose_name="Number of Individuals")
    field = MultiSelectField(max_length=1000, choices=MAJORS, max_choices=3, default=None, blank=True, verbose_name="Field")
    org_type = models.CharField(max_length=1000, choices=ORG_TYPES, default=None, blank=True, verbose_name="Organization Type")


    def __str__(self):
        return self.org.email

    def get_absolute_url(self):
        return reverse('users:orgdemo_detail', kwargs={'pk': self.pk})

class Int(models.Model):
    student = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Student")
    work = MultiSelectField(max_length=1000, choices=WORK, max_choices=4, default=None, blank=True, verbose_name="What do you value most when considering a company?")
    values = MultiSelectField(max_length=1000, choices=VALUES, max_choices=4, default=None, blank=True, verbose_name="Which of these words do you relate to most?")
    env = MultiSelectField(max_length=1000, choices=ENV, max_choices=4, default=None, blank=True, verbose_name="What office environment would you prefer to work in?")
    acts = MultiSelectField(max_length=1000, choices=ACT, max_choices=4, default=None, blank=True, verbose_name="What do you usually do in your spare time?")

    def __str__(self):
        return self.student.email

    def get_absolute_url(self):
        return reverse('users:int_detail', kwargs={'pk': self.pk})

class Exp(models.Model):
    student = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Student")
    role = models.CharField(max_length=1000, default=None, blank=True, verbose_name="Current or Preferred Role")
    field = MultiSelectField(max_length=1000, choices=MAJORS, max_choices=3, default=None, blank=True, verbose_name="Fields")
    skills = MultiSelectField(max_length=1000, choices=SKILLS, max_choices=4, default=None, blank=True, verbose_name="Skills")
    resume = models.FileField(default=None, upload_to='resumes', verbose_name="Resume", null=True, blank=True)

    def __str__(self):
        return self.student.email

    def get_absolute_url(self):
        return reverse('users:exp_detail', kwargs={'pk': self.pk})