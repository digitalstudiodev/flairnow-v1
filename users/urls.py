from django.urls import path, include
from .views import (
    register, register_organization, profile, 
    organization_profile, profile_update, login_view, 
    logout_view, AcademicDetailView, AcademicCreateView, 
    AcademicUpdateView, BackgroundDetailView, BackgroundCreateView, 
    BackgroundUpdateView, ContactDetailView, ContactCreateView, 
    ContactUpdateView, OrganizationContactDetailView, OrganizationContactCreateView, 
    OrganizationContactUpdateView, OrganizationBackgroundDetailView, OrganizationBackgroundUpdateView, 
    OrganizationBackgroundCreateView, InternCommonAppDetailView, InternCommonAppUpdateView, InternCommonAppCreateView,
    ScholarCommonAppDetailView, ScholarCommonAppCreateView, ScholarCommonAppUpdateView
)

app_name = 'users'

urlpatterns = [
    ##registration
    path('register/', register, name='register'),
    path('register-organization/', register_organization, name='register-organization'),
    ##profiles
    path('profile/', profile, name='profile'),
    path('organization-profile/', organization_profile, name='organization-profile'),
    path('profile-update/', profile_update, name='profile-update'),
    ##login + logout
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    ##student academic information
    path('academic/<int:pk>/', AcademicDetailView.as_view(), name='academic-detail'),
    path('academic/new/', AcademicCreateView.as_view(), name='academic-create'),
    path('academic/<int:pk>/update/', AcademicUpdateView.as_view(), name='academic-update'),
    ##student background information
    path('background/<int:pk>/', BackgroundDetailView.as_view(), name='background-detail'),
    path('background/new/', BackgroundCreateView.as_view(), name='background-create'),
    path('background/<int:pk>/update/', BackgroundUpdateView.as_view(), name='background-update'),
    ##student contact information
    path('contact/<int:pk>/', ContactDetailView.as_view(), name='contact-detail'),
    path('contact/new/', ContactCreateView.as_view(), name='contact-create'),
    path('contact/<int:pk>/update/', ContactUpdateView.as_view(), name='contact-update'),
    ##organization contact information
    path('organization-contact/<int:pk>/', OrganizationContactDetailView.as_view(), name='organizationcontact-detail'),
    path('organization-contact/new/', OrganizationContactCreateView.as_view(), name='organizationcontact-create'),
    path('organization-contact/<int:pk>/update/', OrganizationContactUpdateView.as_view(), name='organizationcontact-update'),
    ##organization background information
    path('organization-background/<int:pk>/', OrganizationBackgroundDetailView.as_view(), name='organizationbackground-detail'),
    path('organization-background/new/', OrganizationBackgroundCreateView.as_view(), name='organizationbackground-create'),
    path('organization-background/<int:pk>/update/', OrganizationBackgroundUpdateView.as_view(), name='organizationbackground-update'),
    ##student internship application
    path('internship-common-application/<int:pk>/', InternCommonAppDetailView.as_view(), name='internship-common-application-detail'),
    path('internship-common-application/new/', InternCommonAppCreateView.as_view(), name='internship-common-application-create'),
    path('internship-common-application/<int:pk>/update/', InternCommonAppUpdateView.as_view(), name='internship-common-application-update'),
    ##student scholarship application
    path('scholarship-common-application/<int:pk>/', ScholarCommonAppDetailView.as_view(), name='scholarship-common-application-detail'),
    path('scholarship-common-application/new/', ScholarCommonAppCreateView.as_view(), name='scholarship-common-application-create'),
    path('scholarship-common-application/<int:pk>/update/', ScholarCommonAppUpdateView.as_view(), name='scholarship-common-application-update'),
]