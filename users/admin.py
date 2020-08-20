from django.contrib import admin
from .models import Profile, Manager, User, Org, Resume, Academic

admin.site.register(Profile)
admin.site.register(User)
admin.site.register(Org)
admin.site.register(Resume)
admin.site.register(Academic)

