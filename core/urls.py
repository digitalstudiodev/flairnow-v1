from django.contrib import admin
from django.urls import path
from .views import (
    home, browse, about, contact, partner_contract,
    internship_info, internship_dash, InternshipListView, 
    InternshipDetailView, InternshipCreateView, 
    InternshipUpdateView, InternshipDeleteView
    )

app_name = 'core'

urlpatterns = [
    path('', home, name="home"),
    path('browse', browse, name="browse"),
    path('about', about, name="about"),
    path('contact', contact, name="contact"),
    path('partner-contract', partner_contract, name="partner-contract"),
    path('internship-info', internship_info, name="internship-info"),
    path('internship-dash', internship_dash, name="internship-dash"),
    #internships
    path('internship/', InternshipListView.as_view(), name="internship"),
    path('internship/<int:pk>/', InternshipDetailView.as_view(), name='internship-detail'),
    path('internship/new/', InternshipCreateView.as_view(), name='internship-create'),
    path('internship/<int:pk>/update', InternshipUpdateView.as_view(), name='internship-update'),
    path('internship/<int:pk>/delete', InternshipDeleteView.as_view(), name='internship-delete'),
]
