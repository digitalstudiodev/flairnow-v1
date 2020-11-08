from django.contrib import admin
from .models import (
    Profile, Manager, User, Academic, Background, 
    Contact, OrganizationContact, 
    OrganizationBackground, InternCommonApp
    )

admin.site.register(Profile)
admin.site.register(User)
admin.site.register(Academic)
admin.site.register(Background)
admin.site.register(Contact)
admin.site.register(OrganizationContact)
admin.site.register(OrganizationBackground)
admin.site.register(InternCommonApp)

