from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Internship
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator
from .models import InternshipApplication
from django.views.generic.edit import FormMixin
from django.urls import reverse

def home(request):
    context = {
        'internships': Internship.objects.all()[0:8]
    }
    return render(request, "core/home.html", context)

def about(request):
    context = {
    }
    return render(request, "core/about.html", context)

def contact(request):
    context = {
    }
    return render(request, "core/contact.html", context)

def partner_contract(request):
    context = {
    }
    return render(request, "core/partner_contract.html", context)

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

class InternshipApplicationCreateView(LoginRequiredMixin, CreateView):
    model = InternshipApplication
    success_url = "/users/profile/"
    fields = ['sure']


    def form_valid(self, form):
        internships = self.kwargs["internships"]
        form.instance.student = self.request.user
        form.instance.internship = Internship.objects.all().filter(id=internships)[0]
        match = InternshipApplication.objects.all().filter(internship=form.instance.internship, student=form.instance.student)
        if match:
            messages.warning(self.request,f"You have already applied to this internship. Check on the status below.")
            return redirect("users:profile")
        else:
            form.instance.status = "P"
            messages.success(self.request,f"Congrats you have successfullly applied to this internship!")
            return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super(InternshipApplicationCreateView, self).get_context_data(**kwargs)
        context['internship'] = Internship.objects.all().filter(id=self.kwargs["internships"])[0]
        return context