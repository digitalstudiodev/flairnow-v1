from django.urls import path, include
from .views import (register, profile, profile_update, login_view, logout_view, base, OrgDetailView, OrgCreateView, OrgUpdateView, ResumeDetailView, ResumeCreateView, ResumeUpdateView, AcademicDetailView, AcademicCreateView, AcademicUpdateView, BackgroundDetailView, BackgroundCreateView, BackgroundUpdateView, ContactDetailView, ContactCreateView, ContactUpdateView)

app_name = 'users'

urlpatterns = [
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('profile-update/', profile_update, name='profile-update'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    ##organization
    path('org/<int:pk>/', OrgDetailView.as_view(), name='org-detail'),
    path('org/new/', OrgCreateView.as_view(), name='org-create'),
    path('org/<int:pk>/update/', OrgUpdateView.as_view(), name='org-update'),
    ##resume
    path('resume/<int:pk>/', ResumeDetailView.as_view(), name='resume-detail'),
    path('resume/new/', ResumeCreateView.as_view(), name='resume-create'),
    path('resume/<int:pk>/update/', ResumeUpdateView.as_view(), name='resume-update'),
    ##academic
    path('academic/<int:pk>/', AcademicDetailView.as_view(), name='academic-detail'),
    path('academic/new/', AcademicCreateView.as_view(), name='academic-create'),
    path('academic/<int:pk>/update/', AcademicUpdateView.as_view(), name='academic-update'),
    ##background
    path('background/<int:pk>/', BackgroundDetailView.as_view(), name='background-detail'),
    path('background/new/', BackgroundCreateView.as_view(), name='background-create'),
    path('background/<int:pk>/update/', BackgroundUpdateView.as_view(), name='background-update'),
    ##contact
    path('contact/<int:pk>/', ContactDetailView.as_view(), name='contact-detail'),
    path('contact/new/', ContactCreateView.as_view(), name='contact-create'),
    path('contact/<int:pk>/update/', ContactUpdateView.as_view(), name='contact-update'),
]