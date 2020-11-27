from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, LoginForm, OrgRegisterForm, ContactForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import User, Academic, Background, Contact, OrgContact, OrgBackground, UInternshipApp, UScholarshipApp
from core.models import Internship, Scholarship, InternshipApp, ScholarshipApp, External
from itertools import chain

def register(request):
    form = UserRegisterForm()
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

def register_org(request):
    form = OrgRegisterForm()
    if request.method == 'POST':
        form = OrgRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:login')
    else:
        form = OrgRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required(login_url='users:login')
def profile(request):
    internship_applications = InternshipApp.objects.all().filter(student=request.user)
    scholarship_applications = ScholarshipApp.objects.all().filter(student=request.user)
    applications = sorted(
        chain(internship_applications, scholarship_applications),
        key=lambda instance: instance.date_posted
    )
    context = {
        'applications': applications
    }
    return render(request, 'users/profile.html', context)

@login_required(login_url='users:login')
def org_profile(request):
    contact = OrgContact.objects.all().filter(organization=request.user).first()
    background = OrgBackground.objects.all().filter(organization=request.user).first()
    externalopps = External.objects.all().filter(organization=request.user)
    confirmed = False
    if contact and background:
        confirmed = True
    context = {
        'internships': Internship.objects.all().filter(organization=request.user),
        'scholarships': Scholarship.objects.all().filter(organization=request.user),
        'confirmed': confirmed,
        'externalopps': externalopps,
    }
    return render(request, 'users/org_profile.html', context)

@login_required(login_url='users:login')
def profile_update(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            if request.user.is_student:
                return redirect('users:profile')
            elif request.user.is_organization:
                return redirect('users:org_profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    
    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, 'users/profile_update.html', context)

def logout_view(request):
    logout(request)
    return render(request, 'users/logout.html')

def login_view(request):
    context = {}

    user = request.user
    if user.is_authenticated:
        return redirect('users:profile')

    if request.POST:
        form = LoginForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)
            if user:
                if user.is_student:
                    login(request, user)
                    return redirect('users:profile')
                elif user.is_organization:
                    login(request, user)
                    return redirect('users:org_profile')
    else:
        form = LoginForm()
    context['form'] = form

    return render(request, "users/login.html", context)

class AcademicDetailView(DetailView):
    model = Academic

class AcademicCreateView(LoginRequiredMixin, CreateView):
    model = Academic
    fields = ['school','edu_level','degree','field','gpa','grad_year']

    def form_valid(self, form):
        form.instance.student = self.request.user
        return super().form_valid(form)

class AcademicUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Academic
    fields = ['school','edu_level','degree','field','gpa','grad_year']

    def form_valid(self, form):
        form.instance.student = self.request.user
        return super().form_valid(form)

    def test_func(self):
        obj = self.get_object()
        if obj:
            return True
        return False

class BackgroundDetailView(DetailView):
    model = Background

class BackgroundCreateView(LoginRequiredMixin, CreateView):
    model = Background
    fields = ['gender','sex','race','citizenship','household_size','household_income','first_gen']

    def form_valid(self, form):
        form.instance.student = self.request.user
        return super().form_valid(form)

class BackgroundUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Background
    fields = ['gender','sex','race','citizenship','household_size','household_income','first_gen']

    def form_valid(self, form):
        form.instance.student = self.request.user
        return super().form_valid(form)

    def test_func(self):
        obj = self.get_object()
        if obj:
            return True
        return False

class ContactDetailView(DetailView):
    model = Contact

@login_required(login_url='users:login')
def create_contact(request):
    """
    -> contact create view
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        form.instance.student = request.user        
        if form.is_valid():
            contact = Contact(
                student=request.user,
                phone=request.POST['dob'],
                dob=request.POST['dob'],
                primary_address=request.POST['primary_address'],
                secondary_address=request.POST['secondary_address'],
                zip_code=request.POST['zip_code'],
                city=request.POST['city'],
                state=request.POST['state'],
            )
            contact.save()
            messages.success(request, f'You contact information has been successfully saved!')
            return redirect('users:contact_detail', contact.id)
    else:
        form = ContactForm()
    
    context = {
        'form': form,
    }
    return render(request, 'users/contact_form.html', context)

@login_required(login_url='users:login')
def update_contact(request, pk):
    """
    -> contact update view
    """
    contact = Contact.objects.all().filter(id=pk).first()
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        form.instance.student = request.user        
        if form.is_valid():
            contact.phone = request.POST['phone']
            contact.dob = request.POST['dob']
            contact.primary_address = request.POST['primary_address']
            contact.secondary_address = request.POST['secondary_address']
            contact.zip_code = request.POST['zip_code']
            contact.city = request.POST['city']
            contact.state = request.POST['state']
            
            contact.save()
            messages.success(request, f'Your contact information has been successfully updated!')
            return redirect('users:contact_detail', contact.id)
    else:
        form = ContactForm(instance=contact)
    
    context = {
        'form': form,
    }
    return render(request, 'users/contact_form.html', context)

class OrgContactDetailView(DetailView):
    model = OrgContact

class OrgContactCreateView(LoginRequiredMixin, CreateView):
    model = OrgContact
    fields = ['phone', 'primary_address','secondary_address','zip_code','city', 'state', 'website_link']

    def form_valid(self, form):
        form.instance.organization = self.request.user
        return super().form_valid(form)

class OrgContactUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = OrgContact
    fields = ['phone', 'primary_address','secondary_address','zip_code','city', 'state', 'website_link']

    def form_valid(self, form):
        form.instance.organization = self.request.user
        return super().form_valid(form)

    def test_func(self):
        coap = self.get_object()
        if coap:
            return True
        return False

class OrgBackgroundDetailView(DetailView):
    model = OrgBackground

class OrgBackgroundCreateView(LoginRequiredMixin, CreateView):
    model = OrgBackground
    fields = ['size', 'industry','org_type']

    def form_valid(self, form):
        form.instance.organization = self.request.user
        return super().form_valid(form)

class OrgBackgroundUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = OrgBackground
    fields = ['size', 'industry','org_type']

    def form_valid(self, form):
        form.instance.organization = self.request.user
        return super().form_valid(form)

    def test_func(self):
        coap = self.get_object()
        if coap:
            return True
        return False

class UInternshipAppDetailView(DetailView):
    model = UInternshipApp

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        q1 = UInternshipApp.objects.all()[0]._meta.get_field('q1').verbose_name
        q2 = UInternshipApp.objects.all()[0]._meta.get_field('q2').verbose_name
        context['q1'] = q1
        context['q2'] = q2
        return context

class UInternshipAppCreateView(LoginRequiredMixin, CreateView):
    model = UInternshipApp
    fields = ['q1', 'q2']

    def form_valid(self, form):
        form.instance.student = self.request.user
        return super().form_valid(form)

class UInternshipAppUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = UInternshipApp
    fields = ['q1', 'q2']

    def form_valid(self, form):
        form.instance.student = self.request.user
        return super().form_valid(form)

    def test_func(self):
        obj = self.get_object()
        if obj:
            return True
        return False

class UScholarshipAppDetailView(DetailView):
    model = UScholarshipApp

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        q1 = UScholarshipApp.objects.all()[0]._meta.get_field('q1').verbose_name
        q2 = UScholarshipApp.objects.all()[0]._meta.get_field('q2').verbose_name
        context['q1'] = q1
        context['q2'] = q2
        return context

class UScholarshipAppCreateView(LoginRequiredMixin, CreateView):
    model = UScholarshipApp
    fields = ['q1', 'q2']

    def form_valid(self, form):
        form.instance.student = self.request.user
        return super().form_valid(form)

class UScholarshipAppUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = UScholarshipApp
    fields = ['q1', 'q2']

    def form_valid(self, form):
        form.instance.student = self.request.user
        return super().form_valid(form)

    def test_func(self):
        obj = self.get_object()
        if obj:
            return True
        return False