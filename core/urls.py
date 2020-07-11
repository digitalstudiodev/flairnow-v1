from django.contrib import admin
from django.urls import path
from .views import (home, InternListView, InternDetailView, InternCreateView, InternUpdateView, InternDeleteView, apply_intern)

app_name = 'core'

urlpatterns = [
    path('', home, name="home"),
    path('internships/', InternListView.as_view(), name="internships"),
    path('intern/<int:pk>/', InternDetailView.as_view(), name='intern-detail'),
    path('intern/new/', InternCreateView.as_view(), name='intern-create'),
    path('intern/<int:pk>/update', InternUpdateView.as_view(), name='intern-update'),
    path('intern/<int:pk>/delete', InternDeleteView.as_view(), name='intern-delete'),
    path('apply-intern/<int:pk>/', apply_intern, name='apply-intern'),
]
