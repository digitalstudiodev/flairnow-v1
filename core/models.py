from django.db import models
from django.urls import reverse
from django.utils import timezone
from users.models import Org, User, Coap


class Intern(models.Model):
    title = models.CharField(max_length=100, verbose_name="Position Title")
    company = models.ForeignKey('users.Org', on_delete=models.SET_NULL, blank=True, null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    tag = models.CharField(max_length=100, default="", null=False)
    description = models.TextField(verbose_name="Description", default="")
    requirements = models.TextField(verbose_name="Requirements", default="", help_text="What is required for the position? Education, Experience, etc.")
    duties = models.TextField(verbose_name="Reponsibilities", default="", help_text="What are the reponsibilities related to the position?")
    other = models.TextField(verbose_name="Other", default="", help_text="Include other information such as if position is paid, whether the position is done remotely or in person, or any other additional information.")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('core:intern-detail', kwargs={'pk': self.pk})

class App(models.Model):
    coap = models.ForeignKey('users.Coap', on_delete=models.SET_NULL, blank=True, null=True)
    company = models.ForeignKey('Intern', on_delete=models.SET_NULL, blank=True, null=True)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.pk

    def get_absolute_url(self):
        return reverse('core:app-detail', kwargs={'pk': self.pk})