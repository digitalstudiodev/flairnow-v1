from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, LoginForm, OrgRegisterForm, ContactForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import User, Edu, Demo, Contact, OrgContact, OrgDemo, Int, Exp
from core.models import Internship, Scholarship, InternshipApp, ScholarshipApp, External
from itertools import chain
from django.template import RequestContext

def invalid_error(request, code):
    messages.warning(request, f'Invalid Request {code}')
    return render(request, 'users/404.html')

def invalid_view(request):
    messages.warning(request, f'Invalid Request')
    return render(request, 'users/404.html')

def register(request):
    form = UserRegisterForm()
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register_student.html', {'form': form})

def register_org(request):
    form = OrgRegisterForm()
    if request.method == 'POST':
        form = OrgRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:login')
    else:
        form = OrgRegisterForm()
    return render(request, 'users/register_org.html', {'form': form})

@login_required(login_url='users:login')
def profile(request):
    intern_apps = InternshipApp.objects.all().filter(student=request.user)
    scholar_apps = ScholarshipApp.objects.all().filter(student=request.user)
    apps = sorted(
        chain(intern_apps, scholar_apps),
        key=lambda instance: instance.date_posted
    )
    context = {
        'apps': apps
    }
    return render(request, 'users/profile.html', context)

@login_required(login_url='users:login')
def org_profile(request):
    contact = OrgContact.objects.all().filter(org=request.user).first()
    demo = OrgDemo.objects.all().filter(org=request.user).first()
    ext = External.objects.all().filter(org=request.user)
    confirmed = False
    if contact and demo:
        confirmed = True
    context = {
        'intern': Internship.objects.all().filter(org=request.user),
        'scholar': Scholarship.objects.all().filter(org=request.user),
        'confirmed': confirmed,
        'ext': ext,
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

class EduDetailView(DetailView):
    model = Edu

class EduCreateView(LoginRequiredMixin, CreateView):
    model = Edu
    fields = ['school', 'city', 'state', 'edu_level','degree','major','con','grad_year']

    def form_valid(self, form):
        form.instance.student = self.request.user
        return super().form_valid(form)

class EduUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Edu
    fields = ['school', 'city', 'state', 'edu_level','degree','major','con','grad_year']

    def form_valid(self, form):
        form.instance.student = self.request.user
        return super().form_valid(form)

    def test_func(self):
        obj = self.get_object()
        if obj:
            return True
        return False

class DemoDetailView(DetailView):
    model = Demo

class DemoCreateView(LoginRequiredMixin, CreateView):
    model = Demo
    fields = ['gender','sex','race','cit','house_size','house_income','first_gen']

    def form_valid(self, form):
        form.instance.student = self.request.user
        return super().form_valid(form)

class DemoUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Demo
    fields = ['gender','sex','race','cit','house_size','house_income','first_gen']

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
                street=request.POST['street'],
                apt=request.POST['apt'],
                zip_code=request.POST['zip_code'],
                city=request.POST['city'],
                state=request.POST['state'],
                linkedin=request.POST['linkedin'],
            )
            contact.save()
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
            contact.street = request.POST['street']
            contact.apt = request.POST['apt']
            contact.zip_code = request.POST['zip_code']
            contact.city = request.POST['city']
            contact.state = request.POST['state']
            contact.linkedin = request.POST['linkedin']
            
            contact.save()
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
    fields = ['phone', 'street','apt','zip_code','city', 'state', 'website_link','linkedin']

    def form_valid(self, form):
        form.instance.org = self.request.user
        return super().form_valid(form)

class OrgContactUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = OrgContact
    fields = ['phone', 'street','apt','zip_code','city', 'state', 'website_link','linkedin']

    def form_valid(self, form):
        form.instance.org = self.request.user
        return super().form_valid(form)

    def test_func(self):
        coap = self.get_object()
        if coap:
            return True
        return False

class OrgDemoDetailView(DetailView):
    model = OrgDemo

class OrgDemoCreateView(LoginRequiredMixin, CreateView):
    model = OrgDemo
    fields = ['size','field','org_type']

    def form_valid(self, form):
        form.instance.org = self.request.user
        return super().form_valid(form)

class OrgDemoUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = OrgDemo
    fields = ['size','field','org_type']

    def form_valid(self, form):
        form.instance.org = self.request.user
        return super().form_valid(form)

    def test_func(self):
        obj = self.get_object()
        if obj:
            return True
        return False

class IntDetailView(DetailView):
    model = Int

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        work = Int.objects.all()[0]._meta.get_field('work').verbose_name
        values = Int.objects.all()[0]._meta.get_field('values').verbose_name
        env = Int.objects.all()[0]._meta.get_field('env').verbose_name
        acts = Int.objects.all()[0]._meta.get_field('acts').verbose_name
        context = {
            'work': work,
            'values': values,
            'env': env,
            'acts': acts,
            'object': Int.objects.get(pk=self.object.id)
        }
        return context

class IntCreateView(LoginRequiredMixin, CreateView):
    model = Int
    fields = ['work', 'values', 'env', 'acts']

    def form_valid(self, form):
        form.instance.student = self.request.user
        return super().form_valid(form)

class IntUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Int
    fields = ['work', 'values', 'env', 'acts']

    def form_valid(self, form):
        form.instance.student = self.request.user
        return super().form_valid(form)

    def test_func(self):
        obj = self.get_object()
        if obj:
            return True
        return False

class ExpDetailView(DetailView):
    model = Exp

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        role = Exp.objects.all()[0]._meta.get_field('role').verbose_name
        field = Exp.objects.all()[0]._meta.get_field('field').verbose_name
        skills = Exp.objects.all()[0]._meta.get_field('skills').verbose_name
        context = {
            'role': role,
            'field': field,
            'skills': skills,
            'object': Exp.objects.get(pk=self.object.id)
        }
        return context

class ExpCreateView(LoginRequiredMixin, CreateView):
    model = Exp
    fields = ['role', 'field', 'skills', 'resume']

    def form_valid(self, form):
        form.instance.student = self.request.user
        return super().form_valid(form)

class ExpUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Exp
    fields = ['role', 'field', 'skills', 'resume']

    def form_valid(self, form):
        form.instance.student = self.request.user
        return super().form_valid(form)

    def test_func(self):
        obj = self.get_object()
        if obj:
            return True
        return False