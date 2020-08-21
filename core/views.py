from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Internship
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator

def home(request):
    context = {
        'internships': Internship.objects.all()[0:8]
    }
    return render(request, "core/home.html", context)

def browse(request):
    context = {
        'internships': Internship.objects.all()[0:8]
    }
    return render(request, "core/browse.html", context)

def internship_info(request):
    context = {
    }
    return render(request, "core/internship_info.html", context)

def internship_dash(request):
    page_number = request.GET.get('page')
    paginator = Paginator(Internship.objects.filter(organization=request.user), 5)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'internships': Internship.objects.filter(organization=request.user),
        'page_obj': page_obj

    }
    return render(request, "core/internship_dash.html", context)

class InternshipListView(ListView):
    model = Internship
    template_name = 'core/internship_list.html'  
    context_object_name = 'intern'
    ordering = ['-date_posted']
    paginate_by = 32

class InternshipDetailView(DetailView):
    model = Internship

class InternshipCreateView(LoginRequiredMixin, CreateView):
    model = Internship
    fields = [
        ##basic information
        'title', 'industry', 'start_date', 'end_date', 'number_of_positions', 'description',
        ##education requirements
        'grade_level','degree','gpa',
        ##financial information
        'salary'
        ]

    def form_valid(self, form):
        form.instance.organization = self.request.user
        return super().form_valid(form)

class InternshipUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Internship
    fields = [
        ##basic information
        'title', 'industry', 'start_date', 'end_date', 'number_of_positions', 'description',
        ##education requirements
        'grade_level','degree','gpa',
        ##financial information
        'salary'
        ]

    def form_valid(self, form):
        form.instance.organization = self.request.user
        return super().form_valid(form)

    def test_func(self):
        intern = self.get_object()
        if intern:
            return True
        return False

class InternshipDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Internship
    success_url = '/'

    def test_func(self):
        intern = self.get_object()
        if intern:
            return True
        return False
