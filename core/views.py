from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Intern
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import App

# Create your views here.
def home(request):
    context = {
        'intern': Intern.objects.order_by('-date_posted')[:16]
    }
    return render(request, "core/home.html", context)

class InternListView(ListView):
    model = Intern
    template_name = 'core/interns.html'  
    context_object_name = 'intern'
    ordering = ['-date_posted']
    paginate_by = 32

class InternDetailView(DetailView):
    model = Intern

class InternCreateView(LoginRequiredMixin, CreateView):
    model = Intern
    fields = ['title', 'tag', 'description', 'requirements', 'duties', 'other']

    def form_valid(self, form):
        form.instance.company = self.request.user.org
        return super().form_valid(form)

class InternUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Intern
    fields = ['title', 'tag', 'description', 'requirements', 'duties', 'other']

    def form_valid(self, form):
        form.instance.company = self.request.user.org
        return super().form_valid(form)

    def test_func(self):
        intern = self.get_object()
        if intern:
            return True
        return False

class InternDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Intern
    success_url = '/'

    def test_func(self):
        intern = self.get_object()
        if intern:
            return True
        return False

@login_required(login_url='users:login')
def apply_intern(request, pk):
    try:
        if request.user.coap:
            item = get_object_or_404(Intern, id=pk)
            app, created = App.objects.get_or_create(
                coap=request.user.coap, op=item, org=item.company
                )
            app_qs = App.objects.filter(coap=request.user.coap, op=item, org=item.company)
            messages.success(request, f'Application Submitted!')
            return redirect('users:profile')
    except:
        messages.info(request, f'You must fill out the Common Application!')
        return redirect('users:profile')
    context = {
        'op': item,
    }
    return render(request, "core/application_overview.html", context)