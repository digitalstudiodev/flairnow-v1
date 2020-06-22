from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from PIL import Image
from django.urls import reverse
from django.utils import timezone

ROLES = [
    ("1","Stu"),
    ("2","Org")
]

class Manager(BaseUserManager):
    def create_user(self, first_name, last_name, email, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        if not first_name:
            raise ValueError("Users must have a first name")
        if not last_name:
            raise ValueError("Users must have a last name")

        user = self.model(
            first_name=first_name,
            last_name=last_name,
            email=self.normalize_email(email),
            password=password,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, first_name, last_name, email, password):
        user = self.create_user(
            first_name=first_name,
            last_name=last_name,
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

    first_name = models.CharField(max_length=30, default="", null=False)
    last_name = models.CharField(max_length=30, default="", null=False)
    role = models.CharField(max_length=5, choices=ROLES, default="1", null=False, verbose_name="Role")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

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
    '''
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
    '''

class Org(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Owner")
    date_posted = models.DateTimeField(default=timezone.now)
    name = models.CharField(max_length=100, default="", null=False, verbose_name="Organization Name")
    logo = models.ImageField(default='default_logo.png', upload_to='logo_pics', verbose_name="Logo")
    cover_image = models.ImageField(default='default_cover.png', upload_to='cover_pics', verbose_name="Cover Image")
    location = models.CharField(max_length=300, verbose_name="Location", default="", null=False)
    industry = models.CharField(max_length=30, verbose_name="Industry", default="", null=False)
    website = models.CharField(max_length=300, verbose_name="Website (URL):", default="", null=False)
    description = models.TextField(verbose_name="Description")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('users:org-detail', kwargs={'pk': self.pk})


class Coap(models.Model):
    student = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Student")
    date_posted = models.DateTimeField(default=timezone.now)
    resume = models.FileField(default="sample_resume.pdf", upload_to='resumes', verbose_name="Resume")
    sign = models.CharField(max_length=100, verbose_name="Signature", default="", null=False)
    
    def __str__(self):
        return self.sign

    def get_absolute_url(self):
        return reverse('users:coap-detail', kwargs={'pk': self.pk})