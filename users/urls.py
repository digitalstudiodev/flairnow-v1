from django.urls import path, include
from .views import (register, profile, profile_update, login_view, logout_view, base, OrgDetailView, OrgCreateView, OrgUpdateView, CoapDetailView, CoapCreateView, CoapUpdateView)

app_name = 'users'

urlpatterns = [
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('profile-update/', profile_update, name='profile-update'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    ##Organizations
    path('org/<int:pk>/', OrgDetailView.as_view(), name='org-detail'),
    path('org/new/', OrgCreateView.as_view(), name='org-create'),
    path('org/<int:pk>/update/', OrgUpdateView.as_view(), name='org-update'),
    ##Student Common Application
    path('coap/<int:pk>/', CoapDetailView.as_view(), name='coap-detail'),
    path('coap/new/', CoapCreateView.as_view(), name='coap-create'),
    path('coap/<int:pk>/update/', CoapUpdateView.as_view(), name='coap-update'),
]