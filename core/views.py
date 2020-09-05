from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Internship, Scholarship, InternshipApplication, ScholarshipApplication
from users.models import User, InternCommonApp, ScholarCommonApp
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator
from django.views.generic.edit import FormMixin
from django.urls import reverse
from itertools import chain

##home
"""
this is the home view. 
"""
def home(request):
    internships = Internship.objects.all()[0:4]
    scholarships = Scholarship.objects.all()[0:4]
    opportunities = sorted(
        chain(internships, scholarships),
        key=lambda instance: instance.date_posted
    )
    context = {
        'opportunities': opportunities
    }
    return render(request, "core/home.html", context)

##about
"""
this is the about view. displays information about the venture.
"""
def about(request):
    context = {
    }
    return render(request, "core/about.html", context)

##contact
"""
this is the contact view. this page holds a contact form that newsletter form.
"""
def contact(request):
    context = {
    }
    return render(request, "core/contact.html", context)

##features organization
"""
this is the features orgaanizations view. this present information about the features that organizations get to utilize.
"""
def features_organization(request):
    user_count = User.objects.all().filter(is_student=True).count()
    context = {
        'user_count': user_count
    }
    return render(request, "core/features_organization.html", context)

##features student
"""
this is the features student view. this present information about the features that students get to utilize.
"""
def features_student(request):
    org_count = User.objects.all().filter(is_organization=True).count()
    orgs = User.objects.all().filter(is_organization=True)[0:8]
    context = {
        'org_count': org_count,
        'orgs': orgs,
    }
    return render(request, "core/features_student.html", context)

##partner contract
"""
this is the partner contract view. it is the view that organizations get to before registering on the platform.
"""
def partner_contract(request):
    context = {
    }
    return render(request, "core/partner_contract.html", context)

##browse
"""
this is the browse view. students are able to browse opportunities by categories.
"""
def browse(request):
    internships = Internship.objects.all()[0:4]
    scholarships = Scholarship.objects.all()[0:4]
    opportunities = sorted(
        chain(internships, scholarships),
        key=lambda instance: instance.date_posted
    )
    context = {
        'opportunities': opportunities
    }
    return render(request, "core/browse.html", context)

##internship info for organizations
"""
this is the view that organizations first start to provide internships on the platform. they will 
be informed about the partner contract and other pieces of information.
"""
def internship_info(request):
    context = {
    }
    return render(request, "core/internship_info.html", context)

##scholarship info for organizations
"""
this is the view that organizations first start to provide scholarships on the platform. they will 
be informed about the partner contract and other pieces of information.
"""
def scholarship_info(request):
    context = {
    }
    return render(request, "core/scholarship_info.html", context)


##internship dash for organizations
"""
this is the view that organizations access when they have internships to manage. organizations 
see a list of all of their internships and can go into the detail view for each if they choose to make 
any updates or delete them.
"""
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

##scholarship dash for organizations
"""
this is the view that organizations access when they have scholarships to manage. organizations 
see a list of all of their scholarships and can go into the detail view for each if they choose to make 
any updates or delete them.
"""
def scholarship_dash(request):
    page_number = request.GET.get('page')
    paginator = Paginator(Scholarship.objects.filter(organization=request.user), 5)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'scholarships': Scholarship.objects.filter(organization=request.user),
        'page_obj': page_obj

    }
    return render(request, "core/scholarship_dash.html", context)

##internships list view
"""
this is the category view for internships 
"""
class InternshipListView(ListView):
    model = Internship
    template_name = 'core/internship_list.html'  
    context_object_name = 'intern'
    ordering = ['-date_posted']
    paginate_by = 32

##internship detail view
"""
this is the detailed view for a internship, it provides further information to students before they apply,
and it provides access to update and delete the internship for the organizations. 
"""
class InternshipDetailView(DetailView):
    model = Internship

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_student:
            match = InternshipApplication.objects.all().filter(student=self.request.user)
            if match:
                context['match'] = match[0]  
        applicants = InternshipApplication.objects.all().filter(internship=self.object.id)[0:4]
        context['applicants'] = applicants
        return context

##internship create view
"""
this is form that organizations fill out to create a internship. 
"""
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

##internship update view
"""
this is form that organizations fill out to update a internship. 
"""
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

##internship delete view
"""
this is the view that organizations see to delete a internship.
"""
class InternshipDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Internship
    success_url = '/'

    def test_func(self):
        intern = self.get_object()
        if intern:
            return True
        return False

##internship application create view
"""
this is how students are able to apply to the internships. we create a internship application and
attach it in association with the student and the organization. The organization is able to make updates to
the model by it's status, and students are able to check their application status.
"""
class InternshipApplicationCreateView(LoginRequiredMixin, CreateView):
    model = InternshipApplication
    success_url = "/users/profile/"
    fields = ['confirm']


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

##internship application detail view
"""
this is the internship application detail view. 
"""
class InternshipApplicationDetailView(LoginRequiredMixin, DetailView):
    model = InternshipApplication

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        q1 = InternCommonApp.objects.all()[0]._meta.get_field('q1').verbose_name
        q2 = InternCommonApp.objects.all()[0]._meta.get_field('q2').verbose_name
        q3 = InternCommonApp.objects.all()[0]._meta.get_field('q3').verbose_name
        context['q1'] = q1
        context['q2'] = q2
        context['q3'] = q3
        return context

##internship application update view
"""
this is form that organizations fill out to update a scholarship. 
"""
class InternshipApplicationUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = InternshipApplication
    fields = [
        'status', 
        ]
    template_name_suffix = '_org_update_form'

    def form_valid(self, form):
        form.instance.internship.organization = self.request.user
        messages.success(self.request, f"You have updated the internship application.")
        return super().form_valid(form)

    def test_func(self):
        internship = self.get_object()
        if internship:
            return True
        return False

##scholarships list view
"""
this is the category view for scholarships 
"""
class ScholarshipListView(ListView):
    model = Scholarship
    template_name = 'core/scholarship_list.html'  
    context_object_name = 'scholarship'
    ordering = ['-date_posted']
    paginate_by = 32

##scholarship detail view
"""
this is the detailed view for a scholarship, it provides further information to students before they apply,
and it provides access to update and delete the scholarship for the organizations. 
"""
class ScholarshipDetailView(DetailView):
    model = Scholarship

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_student:
            match = ScholarshipApplication.objects.all().filter(student=self.request.user)
            if match:
                context['match'] = match[0] 
        applicants = ScholarshipApplication.objects.all().filter(scholarship=self.object.id)[0:4]
        context['applicants'] = applicants
        return context

##scholarship create view
"""
this is form that organizations fill out to create a scholarship. 
"""
class ScholarshipCreateView(LoginRequiredMixin, CreateView):
    model = Scholarship
    fields = [
        ##basic information
        'title', 'field', 'description', 'number_of_appliants', 'description',
        ##education requirements
        'grade_level','degree','gpa',
        ##financial information
        'amount'
        ]

    def form_valid(self, form):
        form.instance.organization = self.request.user
        return super().form_valid(form)

##scholarship update view
"""
this is form that organizations fill out to update a scholarship. 
"""
class ScholarshipUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Scholarship
    fields = [
        ##basic information
        'title', 'field', 'description', 'number_of_appliants', 'description',
        ##education requirements
        'grade_level','degree','gpa',
        ##financial information
        'amount'
        ]

    def form_valid(self, form):
        form.instance.organization = self.request.user
        return super().form_valid(form)

    def test_func(self):
        scholarship = self.get_object()
        if scholarship:
            return True
        return False

##scholarship delete view
"""
this is the view that organizations see to delete a scholarship.
"""
class ScholarshipDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Scholarship
    success_url = '/'

    def test_func(self):
        scholarship = self.get_object()
        if scholarship:
            return True
        return False


##scholarship application create view
"""
this is how students are able to apply to the scholarship. we create a scholarship application and
attach it in association with the student and the organization. The organization is able to make updates to
the model by it's status, and students are able to check their application status.
"""
class ScholarshipApplicationCreateView(LoginRequiredMixin, CreateView):
    model = ScholarshipApplication
    success_url = "/users/profile/"
    fields = ['confirm']


    def form_valid(self, form):
        scholarships = self.kwargs["scholarships"]
        form.instance.student = self.request.user
        form.instance.scholarship = Scholarship.objects.all().filter(id=scholarships)[0]
        match = ScholarshipApplication.objects.all().filter(scholarship=form.instance.scholarship, student=form.instance.student)
        if match:
            messages.warning(self.request,f"You have already applied to this scholarship. Check on the status below.")
            return redirect("users:profile")
        else:
            form.instance.status = "P"
            messages.success(self.request,f"Congrats you have successfullly applied to this scholarship!. Check on the status below.")
            return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super(ScholarshipApplicationCreateView, self).get_context_data(**kwargs)
        context['scholarship'] = Scholarship.objects.all().filter(id=self.kwargs["scholarships"])[0]
        return context

##scholarship application detail view
"""
this is the scholarship application detail view. 
"""
class ScholarshipApplicationDetailView(LoginRequiredMixin, DetailView):
    model = ScholarshipApplication

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        q1 = ScholarCommonApp.objects.all()[0]._meta.get_field('q1').verbose_name
        q2 = ScholarCommonApp.objects.all()[0]._meta.get_field('q2').verbose_name
        q3 = ScholarCommonApp.objects.all()[0]._meta.get_field('q3').verbose_name
        context['q1'] = q1
        context['q2'] = q2
        context['q3'] = q3
        return context

##scholarship application update view
"""
this is form that organizations fill out to update a scholarship. 
"""
class ScholarshipApplicationUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = ScholarshipApplication
    fields = [
        'status', 
        ]
    template_name_suffix = '_org_update_form'

    def form_valid(self, form):
        form.instance.scholarship.organization = self.request.user
        messages.success(self.request, f"You have updated the scholarship application.")
        return super().form_valid(form)

    def test_func(self):
        scholarship = self.get_object()
        if scholarship:
            return True
        return False
