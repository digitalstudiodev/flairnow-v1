from django.shortcuts import render
from .models import Intern
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

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
