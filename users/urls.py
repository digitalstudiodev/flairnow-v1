from django.urls import path, include
from .views import (
    register, register_org, 
    profile, org_profile, profile_update,
    login_view, logout_view,
    create_contact, update_contact,ContactDetailView,
    AcademicDetailView, AcademicCreateView, AcademicUpdateView,
    BackgroundDetailView, BackgroundCreateView, BackgroundUpdateView, 
    OrgContactDetailView, OrgContactCreateView, OrgContactUpdateView, 
    OrgBackgroundDetailView, OrgBackgroundUpdateView, OrgBackgroundCreateView, 
    UInternshipAppDetailView, UInternshipAppUpdateView, UInternshipAppCreateView,
    UScholarshipAppDetailView, UScholarshipAppCreateView, UScholarshipAppUpdateView
)

app_name = 'users'

urlpatterns = [
    ##registration
    path('register/', register, name='register'),
    path('register-org/', register_org, name='register_org'),
    ##profiles
    path('profile/', profile, name='profile'),
    path('org-profile/', org_profile, name='org_profile'),
    path('profile-update/', profile_update, name='profile_update'),
    ##login + logout
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    ##student academic information
    path('academic/<int:pk>/', AcademicDetailView.as_view(), name='academic_detail'),
    path('academic/new/', AcademicCreateView.as_view(), name='academic_create'),
    path('academic/<int:pk>/update/', AcademicUpdateView.as_view(), name='academic_update'),
    ##student background information
    path('background/<int:pk>/', BackgroundDetailView.as_view(), name='background_detail'),
    path('background/new/', BackgroundCreateView.as_view(), name='background_create'),
    path('background/<int:pk>/update/', BackgroundUpdateView.as_view(), name='background_update'),
    ##student contact information
    path('contact/<int:pk>/', ContactDetailView.as_view(), name='contact_detail'),
    path('contact/new/', create_contact, name='contact_create'),
    path('contact/<int:pk>/update/', update_contact, name='contact_update'),
    ##organization contact information
    path('org-contact/<int:pk>/', OrgContactDetailView.as_view(), name='orgcontact_detail'),
    path('org-contact/new/', OrgContactCreateView.as_view(), name='orgcontact_create'),
    path('org-contact/<int:pk>/update/', OrgContactUpdateView.as_view(), name='orgcontact_update'),
    ##organization background information
    path('org-background/<int:pk>/', OrgBackgroundDetailView.as_view(), name='orgbackground_detail'),
    path('org-background/new/', OrgBackgroundCreateView.as_view(), name='orgbackground_create'),
    path('org-background/<int:pk>/update/', OrgBackgroundUpdateView.as_view(), name='orgbackground_update'),
    ##student internship application
    path('u-internship-app/<int:pk>/', UInternshipAppDetailView.as_view(), name='u_internship_app_detail'),
    path('u-internship-app/new/', UInternshipAppCreateView.as_view(), name='u_internship_app_create'),
    path('u-internship-app/<int:pk>/update/', UInternshipAppUpdateView.as_view(), name='u_internship_app_update'),
    ##student scholarship application
    path('u-scholarship-app/<int:pk>/', UScholarshipAppDetailView.as_view(), name='u_scholarship_app_detail'),
    path('u-scholarship-app/new/', UScholarshipAppCreateView.as_view(), name='u_scholarship_app_create'),
    path('u-scholarship-app/<int:pk>/update/', UScholarshipAppUpdateView.as_view(), name='u_scholarship_app_update'),
]