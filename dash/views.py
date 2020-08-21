from django.shortcuts import render
from core.models import Internship

def dash(request):
    return render(request, "dash/dash.html")