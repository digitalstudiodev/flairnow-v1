from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Internship, Scholarship, InternshipApplication, ScholarshipApplication, ExternalOpp
from users.models import User, InternCommonApp, ScholarCommonApp
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator
from django.views.generic.edit import FormMixin
from django.urls import reverse
from itertools import chain

def home(request):
    ##home
    """
    this is the home view. 
    """
    internships = Internship.objects.all()[0:4]
    scholarships = Scholarship.objects.all()[0:4]
    externalopps = ExternalOpp.objects.all()[0:4]
    opportunities = sorted(
        chain(internships, scholarships, externalopps),
        key=lambda instance: instance.date_posted
    )
    context = {
        'opportunities': opportunities
    }
    return render(request, "core/home.html", context)

def about(request):
    ##about
    """
    this is the about view. displays information about the venture.
    """
    context = {
    }
    return render(request, "core/about.html", context)

def contact(request):
    ##contact
    """
    this is the contact view. this page holds a contact form that newsletter form.
    """
    context = {
    }
    return render(request, "core/contact.html", context)


def features_organization(request):
    ##features organization
    """
    this is the features orgaanizations view. this present information about the features that organizations get to utilize.
    """
    user_count = User.objects.all().filter(is_student=True).count()
    context = {
        'user_count': user_count
    }
    return render(request, "core/features_organization.html", context)


def features_student(request):
    ##features student
    """
    this is the features student view. this present information about the features that students get to utilize.
    """
    org_count = User.objects.all().filter(is_organization=True).count()
    orgs = User.objects.all().filter(is_organization=True)[0:8]
    context = {
        'org_count': org_count,
        'orgs': orgs,
    }
    return render(request, "core/features_student.html", context)

def partner_contract(request):
    ##partner contract
    """
    this is the partner contract view. it is the view that organizations get to before registering on the platform.
    """
    context = {
    }
    return render(request, "core/partner_contract.html", context)

def browse(request):
    ##browse
    """
    this is the browse view. students are able to browse opportunities by categories.
    """
    internships = Internship.objects.all()[0:4]
    scholarships = Scholarship.objects.all()[0:4]
    externalopps = ExternalOpp.objects.all()[0:4]
    opportunities = sorted(
        chain(internships, scholarships, externalopps),
        key=lambda instance: instance.date_posted
    )
    context = {
        'opportunities': opportunities
    }
    return render(request, "core/browse.html", context)

def internship_info(request):
    ##internship info for organizations
    """
    this is the view that organizations first start to provide internships on the platform. they will 
    be informed about the partner contract and other pieces of information.
    """
    context = {
    }
    return render(request, "core/internship_info.html", context)

def scholarship_info(request):
    ##scholarship info for organizations
    """
    this is the view that organizations first start to provide scholarships on the platform. they will 
    be informed about the partner contract and other pieces of information.
    """
    context = {
    }
    return render(request, "core/scholarship_info.html", context)

def internship_dash(request):
    ##internship dash for organizations
    """
    this is the view that organizations access when they have internships to manage. organizations 
    see a list of all of their internships and can go into the detail view for each if they choose to make 
    any updates or delete them.
    """
    page_number = request.GET.get('page')
    paginator = Paginator(Internship.objects.all().filter(organization=request.user), 5)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'internships': Internship.objects.all().filter(organization=request.user),
        'page_obj': page_obj

    }
    return render(request, "core/internship_dash.html", context)

def scholarship_dash(request):
    ##scholarship dash for organizations
    """
    this is the view that organizations access when they have scholarships to manage. organizations 
    see a list of all of their scholarships and can go into the detail view for each if they choose to make 
    any updates or delete them.
    """
    page_number = request.GET.get('page')
    paginator = Paginator(Scholarship.objects.all().filter(organization=request.user), 5)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'scholarships': Scholarship.objects.all().filter(organization=request.user),
        'page_obj': page_obj

    }
    return render(request, "core/scholarship_dash.html", context)

def externalopp_dash(request):
    ##external opportunity dash for admin
    """
    this is the view that admins access when they have external opportunities to manage. admins 
    see a list of all of the extneral opportunities and can either update or delete them.
    """
    page_number = request.GET.get('page')
    paginator = Paginator(ExternalOpp.objects.filter(organization=request.user), 5)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'externalopps': ExternalOpp.objects.filter(organization=request.user),
        'page_obj': page_obj

    }
    return render(request, "core/externalopp_dash.html", context)

class InternshipListView(ListView):
    ##internships list view
    """
    this is the category view for internships 
    """
    model = Internship
    template_name = 'core/internship_list.html'  
    context_object_name = 'intern'
    ordering = ['-date_posted']
    paginate_by = 32

class InternshipDetailView(DetailView):
    ##internship detail view
    """
    this is the detailed view for a internship, it provides further information to students before they apply,
    and it provides access to update and delete the internship for the organizations. 
    """
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

class InternshipCreateView(LoginRequiredMixin, CreateView):
    ##internship create view
    """
    this is form that organizations fill out to create a internship. 
    """
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
    ##internship update view
    """
    this is form that organizations fill out to update a internship. 
    """
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
    ##internship delete view
    """
    this is the view that organizations see to delete a internship.
    """
    model = Internship
    success_url = '/'

    def test_func(self):
        intern = self.get_object()
        if intern:
            return True
        return False

class InternshipApplicationCreateView(LoginRequiredMixin, CreateView):
    ##internship application create view
    """
    this is how students are able to apply to the internships. we create a internship application and
    attach it in association with the student and the organization. The organization is able to make updates to
    the model by it's status, and students are able to check their application status.
    """
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

class InternshipApplicationDetailView(LoginRequiredMixin, DetailView):
    ##internship application detail view
    """
    this is the internship application detail view. 
    """
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

class InternshipApplicationUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    ##internship application update view
    """
    this is form that organizations fill out to update a scholarship. 
    """
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

class ScholarshipListView(ListView):
    ##scholarships list view
    """
    this is the category view for scholarships 
    """
    model = Scholarship
    template_name = 'core/scholarship_list.html'  
    context_object_name = 'scholarship'
    ordering = ['-date_posted']
    paginate_by = 32

class ScholarshipDetailView(DetailView):
    ##scholarship detail view
    """
    this is the detailed view for a scholarship, it provides further information to students before they apply,
    and it provides access to update and delete the scholarship for the organizations. 
    """
    model = Scholarship

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_student:
            match = ScholarshipApplication.objects.all().filter(student=self.request.user)
            if match:
                context['match'] = True 
        else:
            context['match'] = False
        applicants = ScholarshipApplication.objects.all().filter(scholarship=self.object.id)[0:4]
        context['applicants'] = applicants
        return context

class ScholarshipCreateView(LoginRequiredMixin, CreateView):
    ##scholarship create view
    """
    this is form that organizations fill out to create a scholarship. 
    """
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

class ScholarshipUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    ##scholarship update view
    """
    this is form that organizations fill out to update a scholarship. 
    """
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

class ScholarshipDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    ##scholarship delete view
    """
    this is the view that organizations see to delete a scholarship.
    """
    model = Scholarship
    success_url = '/'

    def test_func(self):
        scholarship = self.get_object()
        if scholarship:
            return True
        return False

class ScholarshipApplicationCreateView(LoginRequiredMixin, CreateView):
    ##scholarship application create view
    """
    this is how students are able to apply to the scholarship. we create a scholarship application and
    attach it in association with the student and the organization. The organization is able to make updates to
    the model by it's status, and students are able to check their application status.
    """
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

class ScholarshipApplicationDetailView(LoginRequiredMixin, DetailView):
    ##scholarship application detail view
    """
    this is the scholarship application detail view. 
    """
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

class ScholarshipApplicationUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    ##scholarship application update view
    """
    this is form that organizations fill out to update a scholarship. 
    """
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

class ExternalOppCreateView(LoginRequiredMixin, CreateView):
    ##external opportunity create view
    """
    this is the create view for the external opportunity model.
    """
    model = ExternalOpp
    fields = ['host','title','type','field','link']
    success_url = '/external-opportunity-dash/'


    def form_valid(self, form):
        form.instance.organization = self.request.user
        return super().form_valid(form)

class ExternalOppUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    ##external opportunity update view
    """
    this is the update view for the external opportunity model.
    """
    model = ExternalOpp
    fields = ['host','title','type','field','link']
    success_url = '/external-opportunity-dash/'

    def form_valid(self, form):
        form.instance.organization = self.request.user
        return super().form_valid(form)

    def test_func(self):
        externalopp = self.get_object()
        if externalopp:
            return True
        return False

class ExternalOppDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    ##external opportunity delete view
    """
    this is the delete view for the external opportunity model.
    """
    model = ExternalOpp
    success_url = '/external-opportunity-dash/'

    def test_func(self):
        externalopp = self.get_object()
        if externalopp:
            return True
        return False