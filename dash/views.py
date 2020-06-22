from django.shortcuts import render
from core.models import Intern

# Create your views here.
def dash(request):
    context = {
        'intern':  Intern.objects.filter(company=request.user.org).order_by('date_posted')
    }
    return render(request, "dash/dash.html", context)