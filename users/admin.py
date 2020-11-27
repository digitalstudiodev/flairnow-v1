from django.contrib import admin
from .models import (
    Profile, Manager, User,
    Academic, Background, Contact,
    OrgContact, OrgBackground, 
    UInternshipApp, UScholarshipApp
    )

admin.site.register(Profile)
admin.site.register(User)
admin.site.register(Academic)
admin.site.register(Background)
admin.site.register(Contact)
admin.site.register(OrgContact)
admin.site.register(OrgBackground)
admin.site.register(UInternshipApp)
admin.site.register(UScholarshipApp)

