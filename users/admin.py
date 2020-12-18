from django.contrib import admin
from .models import (
    Profile, Manager, User,
    Edu, Demo, Contact,
    OrgContact, OrgDemo, 
    Int, Exp
    )

admin.site.register(Profile)
admin.site.register(User)
admin.site.register(Edu)
admin.site.register(Demo)
admin.site.register(Contact)
admin.site.register(OrgContact)
admin.site.register(OrgDemo)
admin.site.register(Int)
admin.site.register(Exp)

