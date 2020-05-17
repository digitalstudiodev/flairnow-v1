from django.db import models
from django.urls import reverse
from django.utils import timezone

TAG_OPTIONS = (
    ("Technology","Technology"),
    ("Finance","Finance"),
    ("Education","Education"),
    ("Engineering","Engineering"),
    ("Other","Other"),
)

class Intern(models.Model):
    title = models.CharField(max_length=100, verbose_name="Position Title")
    company_name = models.CharField(max_length=100, verbose_name="Company Name")
    location = models.CharField(max_length=300, default="", verbose_name="Location", help_text="If the position is remote by insert 'Remote'.")
    logo = models.ImageField(default='default_logo.jpg', upload_to='company_logos', verbose_name="Company/Organization Logo")
    link = models.CharField(max_length=3000, verbose_name="URL")
    date_posted = models.DateTimeField(default=timezone.now)
    tag = models.CharField(max_length=100, choices=TAG_OPTIONS, default="Other", null=False)
    cover_image = models.ImageField(default='default_cover.jpeg', upload_to='position_cover_images', verbose_name="Cover Image")
    description = models.TextField(verbose_name="Description", default="")
    requirements = models.TextField(verbose_name="Requirements", default="", help_text="What is required for the position? Education, Experience, etc.")
    duties = models.TextField(verbose_name="Reponsibilities", default="", help_text="What are the reponsibilities related to the position?")
    other = models.TextField(verbose_name="Other", default="", help_text="Include other information such as if position is paid, whether the position is done remotely or in person, or any other additional information.")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('core:intern-detail', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)