from django.contrib import admin
from django.urls import path
from .views import (
    home, browse, about, contact, partner_contract,
    internship_info, internship_dash, scholarship_info, features_organization, 
    features_student, InternshipListView, 
    InternshipDetailView, InternshipCreateView, 
    InternshipUpdateView, InternshipDeleteView, InternshipApplicationCreateView, InternshipApplicationDetailView,
    ScholarshipListView, ScholarshipDetailView, ScholarshipCreateView, ScholarshipUpdateView,
    ScholarshipDeleteView, ScholarshipApplicationCreateView
    )

app_name = 'core'

urlpatterns = [
    path('', home, name="home"),
    path('browse', browse, name="browse"),
    path('about', about, name="about"),
    path('contact', contact, name="contact"),
    path('features-organization', features_organization, name="features-organization"),
    path('features-student', features_student, name="features-student"),
    path('partner-contract', partner_contract, name="partner-contract"),
    path('internship-info', internship_info, name="internship-info"),
    path('scholarship-info', scholarship_info, name="scholarship-info"),
    path('internship-dash', internship_dash, name="internship-dash"),
    ##internships
    path('internship/', InternshipListView.as_view(), name="internship"),
    path('internship/<int:pk>/', InternshipDetailView.as_view(), name='internship-detail'),
    path('internship/new/', InternshipCreateView.as_view(), name='internship-create'),
    path('internship/<int:pk>/update', InternshipUpdateView.as_view(), name='internship-update'),
    path('internship/<int:pk>/delete', InternshipDeleteView.as_view(), name='internship-delete'),
    path('internship/<int:internships>/apply', InternshipApplicationCreateView.as_view(), name='internship-application-create'),
    path('internship-application/<int:pk>/', InternshipApplicationDetailView.as_view(), name='internship-application-detail'),
    ##scholarships
    path('scholarship/', ScholarshipListView.as_view(), name="scholarship"),
    path('scholarship/<int:pk>/', ScholarshipDetailView.as_view(), name='scholarship-detail'),
    path('scholarship/new/', ScholarshipCreateView.as_view(), name='scholarship-create'),
    path('scholarship/<int:pk>/update', ScholarshipUpdateView.as_view(), name='scholarship-update'),
    path('scholarship/<int:pk>/delete', ScholarshipDeleteView.as_view(), name='scholarship-delete'),
    path('scholarship/<int:scholarships>/apply', ScholarshipApplicationCreateView.as_view(), name='scholarship-application-create'),
]
