from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, LoginForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import User, Org, Coap
from core.models import Intern

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

@login_required(login_url='users:login')
def profile(request):
    return render(request, 'users/profile.html')

@login_required(login_url='users:login')
def profile_update(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('users:profile')
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
                login(request, user)
                return redirect('users:profile')
    else:
        form = LoginForm()
    context['form'] = form

    return render(request, "users/login.html", context)

def base(request):
    return render(request, "users/base.html")


class OrgDetailView(DetailView):
    model = Org

class OrgCreateView(LoginRequiredMixin, CreateView):
    model = Org
    fields = ['name', 'logo', 'cover_image', 'location', 'industry', 'website', 'description']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class OrgUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Org
    fields = ['name', 'logo', 'cover_image', 'location', 'industry', 'website', 'description']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def test_func(self):
        org = self.get_object()
        if org:
            return True
        return False

class CoapDetailView(DetailView):
    model = Coap

class CoapCreateView(LoginRequiredMixin, CreateView):
    model = Coap
    fields = ['resume','sign']

    def form_valid(self, form):
        form.instance.student = self.request.user
        return super().form_valid(form)

class CoapUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Coap
    fields = ['resume','sign']

    def form_valid(self, form):
        form.instance.student = self.request.user
        return super().form_valid(form)

    def test_func(self):
        coap = self.get_object()
        if coap:
            return True
        return False
