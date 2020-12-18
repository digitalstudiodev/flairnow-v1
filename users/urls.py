from django.urls import path, include
from .views import (
    register, register_org, 
    profile, org_profile, profile_update,
    login_view, logout_view,
    create_contact, update_contact,ContactDetailView,
    EduDetailView, EduCreateView, EduUpdateView,
    DemoDetailView, DemoCreateView, DemoUpdateView, 
    OrgContactDetailView, OrgContactCreateView, OrgContactUpdateView, 
    OrgDemoDetailView, OrgDemoUpdateView, OrgDemoCreateView, 
    IntDetailView, IntUpdateView, IntCreateView,
    ExpDetailView, ExpCreateView, ExpUpdateView
)

app_name = 'users'

urlpatterns = [
    #registration
    path('register/', register, name='register'),
    path('register-org/', register_org, name='register_org'),
    #profiles
    path('profile/', profile, name='profile'),
    path('org-profile/', org_profile, name='org_profile'),
    path('profile-update/', profile_update, name='profile_update'),
    #login + logout
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    #student education inf0
    path('edu/<int:pk>/', EduDetailView.as_view(), name='edu_detail'),
    path('edu/new/', EduCreateView.as_view(), name='edu_create'),
    path('edu/<int:pk>/update/', EduUpdateView.as_view(), name='edu_update'),
    #student demographics info
    path('demo/<int:pk>/', DemoDetailView.as_view(), name='demo_detail'),
    path('demo/new/', DemoCreateView.as_view(), name='demo_create'),
    path('demo/<int:pk>/update/', DemoUpdateView.as_view(), name='demo_update'),
    #student contact info
    path('contact/<int:pk>/', ContactDetailView.as_view(), name='contact_detail'),
    path('contact/new/', create_contact, name='contact_create'),
    path('contact/<int:pk>/update/', update_contact, name='contact_update'),
    #organization contact information
    path('org-contact/<int:pk>/', OrgContactDetailView.as_view(), name='orgcontact_detail'),
    path('org-contact/new/', OrgContactCreateView.as_view(), name='orgcontact_create'),
    path('org-contact/<int:pk>/update/', OrgContactUpdateView.as_view(), name='orgcontact_update'),
    #organization demographics information
    path('org-demo/<int:pk>/', OrgDemoDetailView.as_view(), name='orgdemo_detail'),
    path('org-demo/new/', OrgDemoCreateView.as_view(), name='orgdemo_create'),
    path('org-demo/<int:pk>/update/', OrgDemoUpdateView.as_view(), name='orgdemo_update'),
    #student interests
    path('int/<int:pk>/', IntDetailView.as_view(), name='int_detail'),
    path('int/new/', IntCreateView.as_view(), name='int_create'),
    path('int/<int:pk>/update/', IntUpdateView.as_view(), name='int_update'),
    #student experience
    path('exp/<int:pk>/', ExpDetailView.as_view(), name='exp_detail'),
    path('exp/new/', ExpCreateView.as_view(), name='exp_create'),
    path('exp/<int:pk>/update/', ExpUpdateView.as_view(), name='exp_update'),
]