from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, LoginForm, OrgRegisterForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import User, Resume, Academic, Background, Contact, OrganizationContact, OrganizationBackground, InternCommonApp
from core.models import Internship

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

def register_organization(request):
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
    context = {
    }
    return render(request, 'users/profile.html', context)

@login_required(login_url='users:login')
def organization_profile(request):
    context = {
        'internships': Internship.objects.filter(organization=request.user)
    }
    return render(request, 'users/organization_profile.html', context)

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
                return redirect('users:organization-profile')
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
                    return redirect('users:organization-profile')
    else:
        form = LoginForm()
    context['form'] = form

    return render(request, "users/login.html", context)

class ResumeDetailView(DetailView):
    model = Resume

class ResumeCreateView(LoginRequiredMixin, CreateView):
    model = Resume
    fields = ['resume']

    def form_valid(self, form):
        form.instance.student = self.request.user
        return super().form_valid(form)

class ResumeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Resume
    fields = ['resume']

    def form_valid(self, form):
        form.instance.student = self.request.user
        return super().form_valid(form)

    def test_func(self):
        coap = self.get_object()
        if coap:
            return True
        return False

class AcademicDetailView(DetailView):
    model = Academic

class AcademicCreateView(LoginRequiredMixin, CreateView):
    model = Academic
    fields = ['college','current_grade_level','degree_in_pursuit','field','sat_score','act_score','gpa','expected_grad_year']

    def form_valid(self, form):
        form.instance.student = self.request.user
        return super().form_valid(form)

class AcademicUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Academic
    fields = ['college','current_grade_level','degree_in_pursuit','field','sat_score','act_score','gpa','expected_grad_year']

    def form_valid(self, form):
        form.instance.student = self.request.user
        return super().form_valid(form)

    def test_func(self):
        coap = self.get_object()
        if coap:
            return True
        return False

class BackgroundDetailView(DetailView):
    model = Background

class BackgroundCreateView(LoginRequiredMixin, CreateView):
    model = Background
    fields = ['gender','sexual_orientation','race','citizenship','household_size','household_income','first_gen']

    def form_valid(self, form):
        form.instance.student = self.request.user
        return super().form_valid(form)

class BackgroundUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Background
    fields = ['gender','sexual_orientation','race','citizenship','household_size','household_income','first_gen']

    def form_valid(self, form):
        form.instance.student = self.request.user
        return super().form_valid(form)

    def test_func(self):
        coap = self.get_object()
        if coap:
            return True
        return False

class ContactDetailView(DetailView):
    model = Contact

class ContactCreateView(LoginRequiredMixin, CreateView):
    model = Contact
    fields = ['phone_number', 'date_of_birth','primary_address','zip_code','city','state']

    def form_valid(self, form):
        form.instance.student = self.request.user
        return super().form_valid(form)

class ContactUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Contact
    fields = ['phone_number', 'date_of_birth','primary_address','zip_code','city','state']

    def form_valid(self, form):
        form.instance.student = self.request.user
        return super().form_valid(form)

    def test_func(self):
        coap = self.get_object()
        if coap:
            return True
        return False

class OrganizationContactDetailView(DetailView):
    model = OrganizationContact

class OrganizationContactCreateView(LoginRequiredMixin, CreateView):
    model = OrganizationContact
    fields = ['phone_number', 'primary_address','zip_code','city','state', 'website_link', 'facebook_link', 'linkedin_link', 'twitter_link']

    def form_valid(self, form):
        form.instance.organization = self.request.user
        return super().form_valid(form)

class OrganizationContactUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = OrganizationContact
    fields = ['phone_number', 'primary_address','zip_code','city','state', 'website_link', 'facebook_link', 'linkedin_link', 'twitter_link']

    def form_valid(self, form):
        form.instance.organization = self.request.user
        return super().form_valid(form)

    def test_func(self):
        coap = self.get_object()
        if coap:
            return True
        return False

class OrganizationBackgroundDetailView(DetailView):
    model = OrganizationBackground

class OrganizationBackgroundCreateView(LoginRequiredMixin, CreateView):
    model = OrganizationBackground
    fields = ['size', 'industry','type']

    def form_valid(self, form):
        form.instance.organization = self.request.user
        return super().form_valid(form)

class OrganizationBackgroundUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = OrganizationBackground
    fields = ['size', 'industry','type']

    def form_valid(self, form):
        form.instance.organization = self.request.user
        return super().form_valid(form)

    def test_func(self):
        coap = self.get_object()
        if coap:
            return True
        return False

class InternCommonAppDetailView(DetailView):
    model = InternCommonApp

class InternCommonAppCreateView(LoginRequiredMixin, CreateView):
    model = InternCommonApp
    fields = ['q1', 'q2','q3']

    def form_valid(self, form):
        form.instance.student = self.request.user
        return super().form_valid(form)

class InternCommonAppUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = InternCommonApp
    fields = ['q1', 'q2','q3']

    def form_valid(self, form):
        form.instance.student = self.request.user
        return super().form_valid(form)

    def test_func(self):
        coap = self.get_object()
        if coap:
            return True
        return False