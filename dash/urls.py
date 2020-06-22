from django.urls import path, include
from .views import dash

app_name = 'dash'

urlpatterns = [
    path('dash/', dash, name='dash'),
]