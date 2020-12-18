from django.contrib import admin
from django.urls import path
from .views import (
    #global
    home, browse, about, contact, partner_contract, features_org, features_student, 
    #intenship app
    InternshipAppCreateView, InternshipAppDetailView, InternshipAppUpdateView,
    #scholarship app
    ScholarshipAppCreateView, ScholarshipAppUpdateView, ScholarshipAppDetailView,
    #internships
    create_internship, update_internship, InternshipDetailView, InternshipDeleteView,
    internship_list, internship_info, internship_dash, InternshipApplicants,
    #scholarships
    create_scholarship, update_scholarship, ScholarshipDetailView, ScholarshipDeleteView, 
    scholarship_list, scholarship_info, scholarship_dash, ScholarshipApplicants,
    #external
    ExternalCreateView, ExternalUpdateView, ExternalDeleteView, external_dash,
    )

app_name = 'core'

urlpatterns = [
    #global
    path('', home, name="home"),
    path('browse', browse, name="browse"),
    path('about', about, name="about"),
    path('contact', contact, name="contact"),
    path('features-org', features_org, name="features_org"),
    path('features-student', features_student, name="features_student"),
    path('partner-contract', partner_contract, name="partner_contract"),
    #internships
    path('internship/', internship_list, name="internship"),
    path('internship/<int:pk>/', InternshipDetailView.as_view(), name='internship_detail'),
    path('internship/new/', create_internship, name='internship_create'),
    path('internship/<int:pk>/update', update_internship, name='internship_update'),
    path('internship/<int:pk>/delete', InternshipDeleteView.as_view(), name='internship_delete'),
    path('internship/<int:internships>/apply', InternshipAppCreateView.as_view(), name='internship_app_create'),
    path('internship/<int:pk>/applicants', InternshipApplicants.as_view(), name="internship_applicants"),
    path('internship-app/<int:pk>/', InternshipAppDetailView.as_view(), name='internship_app_detail'),
    path('internship-app/<int:pk>/update', InternshipAppUpdateView.as_view(), name='internship_app_update'),
    path('internship-info', internship_info, name="internship_info"),
    path('internship-dash', internship_dash, name="internship_dash"),
    #scholarships
    path('scholarship/', scholarship_list, name="scholarship"),
    path('scholarship/<int:pk>/', ScholarshipDetailView.as_view(), name='scholarship_detail'),
    path('scholarship/new/', create_scholarship, name='scholarship_create'),
    path('scholarship/<int:pk>/update', update_scholarship, name='scholarship_update'),
    path('scholarship/<int:pk>/delete', ScholarshipDeleteView.as_view(), name='scholarship_delete'),
    path('scholarship/<int:scholarships>/apply', ScholarshipAppCreateView.as_view(), name='scholarship_app_create'),
    path('scholarship/<int:pk>/applicants', ScholarshipApplicants.as_view(), name="scholarship_applicants"),
    path('scholarship-app/<int:pk>/', ScholarshipAppDetailView.as_view(), name='scholarship_app_detail'),
    path('scholarship-app/<int:pk>/update', ScholarshipAppUpdateView.as_view(), name='scholarship_app_update'),
    path('scholarship-info', scholarship_info, name="scholarship_info"),
    path('scholarship-dash', scholarship_dash, name="scholarship_dash"),
    #external opportunities
    path('external-create/', ExternalCreateView.as_view(), name="external_create"),
    path('external/<int:pk>/update', ExternalUpdateView.as_view(), name="external_update"),
    path('external/<int:pk>/delete', ExternalDeleteView.as_view(), name="external_delete"),
    path('external-dash/', external_dash, name="external_dash"),
]
