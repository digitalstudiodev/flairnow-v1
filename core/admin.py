from django.contrib import admin
from .models import Internship, InternshipApplication, Scholarship, ScholarshipApplication, ExternalOpp

admin.site.register(Internship)
admin.site.register(InternshipApplication)
admin.site.register(Scholarship)
admin.site.register(ScholarshipApplication)
admin.site.register(ExternalOpp)
