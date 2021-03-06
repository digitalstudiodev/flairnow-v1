from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Internship, Scholarship, InternshipApp, ScholarshipApp, External
from users.models import User, Int, Exp
from .forms import InternshipForm, ScholarshipForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator
from django.views.generic.edit import FormMixin
from django.urls import reverse
from itertools import chain
from blog.models import Post
import datetime
from django.core.mail import send_mail
from flairnow.settings import EMAIL_HOST_USER

def home(request):
    """
    -> home page
    """
    internships = Internship.objects.all()[0:4]
    scholarships = Scholarship.objects.all()[0:4]
    external_int = External.objects.all().filter(type="EIN")[0:4]
    external_sc = External.objects.all().filter(type="ESC")[0:4]
    opportunities = sorted(
        chain(internships, scholarships, external_int, external_sc),
        key=lambda instance: instance.date_posted
    )
    posts = Post.objects.all()[0:4]
    context = {
        'opportunities': opportunities,
        'posts': posts,
    }
    return render(request, "core/home.html", context)

def about(request):
    """
    -> about page
    """
    context = {
    }
    return render(request, "core/about.html", context)

def contact(request):
    """
    -> general contact
    """
    context = {
    }
    return render(request, "core/contact.html", context)

def features_org(request):
    """
    -> info on features for orgs
    """
    user_count = User.objects.all().filter(is_student=True).count()
    context = {
        'user_count': user_count
    }
    return render(request, "core/features_org.html", context)

def features_student(request):
    """
    -> info on features for students
    """
    org_count = User.objects.all().filter(is_organization=True).count()
    orgs = User.objects.all().filter(is_organization=True)[0:8]
    posts = Post.objects.all()[0:4]
    context = {
        'org_count': org_count,
        'orgs': orgs,
        'posts': posts,
    }
    return render(request, "core/features_student.html", context)

def partner_contract(request):
    """
    -> info on goals for orgs
    """
    context = {
    }
    return render(request, "core/partner_contract.html", context)

def browse(request):
    """
    -> browse view
    """
    #grabbing each opportunity type
    internships = Internship.objects.all()[0:4]
    scholarships = Scholarship.objects.all()[0:4]
    external_int = External.objects.all().filter(type="EIN")[0:4]
    external_sc = External.objects.all().filter(type="ESC")[0:4]
    #sorting them by date
    opportunities = sorted(
        chain(internships, scholarships, external_int, external_sc),
        key=lambda instance: instance.date_posted
    )
    #grabbing the latest blog posts
    posts = Post.objects.all()[0:4]
    #exporting context
    context = {
        'opportunities': opportunities,
        'posts': posts,
    }
    return render(request, "core/browse.html", context)

def internship_info(request):
    """
    -> info on internships for orgs
    """
    context = {
    }
    return render(request, "core/internship_info.html", context)

def scholarship_info(request):
    """
    -> info on scholarships for orgs
    """
    context = {
    }
    return render(request, "core/scholarship_info.html", context)

def internship_dash(request):
    """
    -> internship dashboard
    -> allows management of internships
    """
    #paginating internship objects
    paginator = Paginator(Internship.objects.all().filter(org=request.user), 5)
    #grabbing page number
    page_number = request.GET.get('page')
    #paginated object
    page_obj = paginator.get_page(page_number)
    #exporting context
    context = {
        'internships': Internship.objects.all().filter(org=request.user),
        'page_obj': page_obj

    }
    return render(request, "core/internship_dash.html", context)

def scholarship_dash(request):
    """
    -> scholarship dashboard
    -> allows management of scholarships
    """
    #paginating scholarship objects
    paginator = Paginator(Scholarship.objects.all().filter(org=request.user), 5)
    #grabbing page number
    page_number = request.GET.get('page')
    #paginated object
    page_obj = paginator.get_page(page_number)
    #exporting context
    context = {
        'scholarships': Scholarship.objects.all().filter(org=request.user),
        'page_obj': page_obj

    }
    return render(request, "core/scholarship_dash.html", context)

def external_dash(request):
    """
    -> external dashboard
    -> allows management of external opportunities
    """
    #paginating external objects
    paginator = Paginator(External.objects.filter(org=request.user), 5)
    #grabbing page number
    page_number = request.GET.get('page')
    #paginated object
    page_obj = paginator.get_page(page_number)
    #exporting context
    context = {
        'externalopps': External.objects.filter(org=request.user),
        'page_obj': page_obj

    }
    return render(request, "core/external_dash.html", context)

def internship_list(request):
    """
    -> category view for internships 
    """
    #grabbing all internal internships
    internships = Internship.objects.all()
    #grabbing all external internships
    external = External.objects.all().filter(type="EIN")
    #sorting them by date
    opportunities = sorted(
        chain(internships, external),
        key=lambda instance: instance.date_posted
    )
    #paginating internship objects
    paginator = Paginator(opportunities, 32)
    #grabbing page number
    page_number = request.GET.get('page')
    #paginated object
    page_obj = paginator.get_page(page_number)
    #exporting context
    context = {
        'internships': opportunities,
        'page_obj': page_obj

    }
    return render(request, "core/internship_list.html", context)

def scholarship_list(request):
    """
    -> category view for scholarships 
    """
    #grabbing all internal scholarships
    scholarships = Scholarship.objects.all()
    #grabbing all external scholarships
    external = External.objects.all().filter(type="ESC")
    #sorting them by date
    opportunities = sorted(
        chain(scholarships, external),
        key=lambda instance: instance.date_posted
    )
    #paginating scholarship objects
    paginator = Paginator(opportunities, 32)
    #grabbing page number
    page_number = request.GET.get('page')
    #paginated object
    page_obj = paginator.get_page(page_number)
    #exporting context
    context = {
        'scholarships': opportunities,
        'page_obj': page_obj

    }
    return render(request, "core/scholarship_list.html", context)

class InternshipDetailView(DetailView):
    """
    -> internship detail view
    -> provides info to students before they apply
    -> allows orgs to update and delete the internship 
    """
    model = Internship

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        '''
        -> checking if user.is_student has completed their profile. 
        -> checking if user.is_student applied to the internship already
        -> collecting the associated internship applications for orgs to view
        '''
        if self.request.user.is_authenticated:
            context['status'] = False 
            user = self.request.user
            #checking status
            try:
                if user.contact and user.demo and user.edu and user.int and user.exp:
                    context['status'] = True
            except: pass 
            #checkig match
            match = InternshipApp.objects.all().filter(student=user, intern=self.object.id)
            if match:
                context['match'] = True
            #collecting applicants
            applicants = InternshipApp.objects.all().filter(intern=self.object.id)
            #checking if expired

            if applicants:
                context['applicants'] = applicants
        else:
            pass
        return context

@login_required(login_url='users:login')
def create_internship(request):
    """
    -> internship create view
    """
    if request.method == 'POST':
        form = InternshipForm(request.POST)
        form.instance.org = request.user        
        if form.is_valid():
            title = request.POST['title']
            internship = Internship(
                org=request.user,
                title=title,
                field=request.POST['field'],
                desc=request.POST['desc'],
                pos=request.POST['pos'],
                edu_level=request.POST['edu_level'],
                degree=request.POST['degree'],
                amount=request.POST['amount'],
                valid_date=request.POST['valid_date'],
                city=request.POST['city'],
                state=request.POST['state'],
            )
            internship.save()
            messages.success(request, f'{title} has been successfully created!')
            return redirect('core:internship_dash')
    else:
        form = InternshipForm()
    
    context = {
        'form': form,
    }
    return render(request, 'core/internship_form.html', context)

@login_required(login_url='users:login')
def update_internship(request, pk):
    """
    -> internship update view
    """
    internship = Internship.objects.all().filter(id=pk).first()
    if request.method == 'POST':
        form = InternshipForm(request.POST, instance=internship)
        form.instance.org = request.user        
        if form.is_valid():
            title = request.POST['title']
            internship.title = title
            internship.field = request.POST['field']
            internship.desc = request.POST['desc']
            internship.pos = request.POST['pos']
            internship.edu_level = request.POST['edu_level']
            internship.degree = request.POST['degree']
            internship.amount = request.POST['amount']
            internship.valid_date = request.POST['valid_date']
            internship.city = request.POST['city']
            internship.state = request.POST['state']
            
            internship.save()
            messages.success(request, f'{title} has been successfully updated!')
            return redirect('core:internship_detail', internship.id)
    else:
        form = InternshipForm(instance=internship)
    
    context = {
        'form': form,
    }
    return render(request, 'core/internship_form.html', context)

class InternshipDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    -> internship delete view
    """
    model = Internship
    success_url = '/internship-dash'

    def test_func(self):
        obj = self.get_object()
        if obj:
            return True
        return False

class InternshipAppCreateView(LoginRequiredMixin, CreateView):
    """
    -> internship app create view
    """
    model = InternshipApp
    success_url = "/users/profile/"
    fields = ['cover','confirm']


    def form_valid(self, form):
        #grabbing internship primary key
        internships = self.kwargs["internships"]
        #setting the student and internship
        form.instance.student = self.request.user
        form.instance.intern = Internship.objects.all().filter(id=internships)[0]
        #determing whether student already applied to internship
        match = InternshipApp.objects.all().filter(intern=form.instance.intern, student=form.instance.student)
        if match:
            messages.warning(self.request,f"You have already applied to this internship. Check on the status below.")
            return redirect("users:profile")
        else:
            form.instance.status = "P"
            app_title = form.instance.intern.title
            messages.success(self.request,f"Congrats you have successfullly applied to this internship!")
            send_mail(
                f"Congrats you have successfullly applied {app_title}!", 
                f"Congrats you have successfullly applied {app_title}!", 
                EMAIL_HOST_USER, 
                [form.instance.student.email], 
                fail_silently = False,
                html_message=f"<h1>Thank you for applying to {app_title}!</h1><p>Your application is currently being reviewed. Please <a href='https://www.flairnow.org/users/login'>log in</a> to your profile to view the status of your application. </p>",
            )
            return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super(InternshipAppCreateView, self).get_context_data(**kwargs)
        context['internship'] = Internship.objects.all().filter(id=self.kwargs["internships"])[0]
        return context

class InternshipApplicants(LoginRequiredMixin, DetailView):
    """
    -> applicants
    """
    model = Internship
    template_name = "core/internshipapplicants_detail.html"

    def get_context_data(self, **kwargs):
        context = super(InternshipApplicants, self).get_context_data(**kwargs)
        context = {
            'object': Internship.objects.all().filter(id=self.kwargs["pk"])[0],
            'applicants': InternshipApp.objects.all().filter(intern=self.kwargs["pk"]),
        } 
        return context

class InternshipAppDetailView(LoginRequiredMixin, DetailView):
    """
    -> internship app detail view
    """
    model = InternshipApp

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class InternshipAppUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    -> internship app update view
    """
    model = InternshipApp
    fields = [
        'status', 
        ]
    template_name_suffix = '_org_update_form'

    def form_valid(self, form):
        form.instance.intern.org = self.request.user
        messages.success(self.request, f"You have updated the internship application.")
        app = InternshipApp.objects.all().filter(id=self.object.id).first()
        app_title = app.intern.title
        send_mail(
            f"Your Application For {app_title} Has Been Updated!", 
            f"Your Application For {app_title} Has Been Updated!",  
            EMAIL_HOST_USER, 
            [app.student.email], 
            fail_silently = False,
            html_message=f"<h1>Thank you for applying to {app_title}!</h1><p>Your application has been reviewed. Please <a href='https://www.flairnow.org/users/login'>log in</a> to your profile to view the status of your application.</p>",
        )
        return super().form_valid(form)

    def test_func(self):
        obj = self.get_object()
        if obj:
            return True
        return False

class ScholarshipDetailView(DetailView):
    """
    -> scholarship detail view
    -> provides info to students before they apply
    -> allows orgs to update and delete the internship 
    """
    model = Scholarship

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        '''
        -> checking if user.is_student has completed their profile. 
        -> checking if user.is_student applied to the scholarship already
        -> collecting the associated scholarship applications for orgs to view
        '''
        if self.request.user.is_authenticated:
            context['status'] = False 
            user = self.request.user
            #checking status
            try:
                if user.contact and user.demo and user.edu and user.int and user.exp:
                    context['status'] = True
            except: pass 
            #checkig match
            match = ScholarshipApp.objects.all().filter(student=self.request.user, scholar=self.object.id)
            if match:
                context['match'] = True
            #collecting applicants
            applicants = ScholarshipApp.objects.all().filter(scholar=self.object.id)
            if applicants:
                context['applicants'] = applicants
        else:
            pass
        return context

@login_required(login_url='users:login')
def create_scholarship(request):
    """
    -> scholarship create view
    """
    if request.method == 'POST':
        form = ScholarshipForm(request.POST)
        form.instance.org = request.user        
        if form.is_valid():
            title = request.POST['title']
            scholarship = Scholarship(
                org=request.user,
                title=title,
                field=request.POST['field'],
                desc=request.POST['desc'],
                pos=request.POST['pos'],
                edu_level=request.POST['edu_level'],
                degree=request.POST['degree'],
                amount=request.POST['amount'],
                valid_date=request.POST['valid_date'],
                city=request.POST['city'],
                state=request.POST['state'],
            )
            scholarship.save()
            messages.success(request, f'{title} has been successfully created!')
            return redirect('core:scholarship_dash')
    else:
        form = ScholarshipForm()
    
    context = {
        'form': form,
    }
    return render(request, 'core/scholarship_form.html', context)

@login_required(login_url='users:login')
def update_scholarship(request, pk):
    """
    -> scholarship update view
    """
    scholarship = Scholarship.objects.all().filter(id=pk).first()
    if request.method == 'POST':
        form = ScholarshipForm(request.POST, instance=scholarship)
        form.instance.org = request.user        
        if form.is_valid():
            title = request.POST['title']
            scholarship.title = title
            scholarship.field = request.POST['field']
            scholarship.desc = request.POST['desc']
            scholarship.pos = request.POST['pos']
            scholarship.edu_level = request.POST['edu_level']
            scholarship.degree = request.POST['degree']
            scholarship.amount = request.POST['amount']
            scholarship.valid_date = request.POST['valid_date']
            scholarship.city = request.POST['city']
            scholarship.state = request.POST['state']
            
            scholarship.save()
            messages.success(request, f'{title} has been successfully updated!')
            return redirect('core:scholarship_detail', scholarship.id)
    else:
        form = InternshipForm(instance=scholarship)
    
    context = {
        'form': form,
    }
    return render(request, 'core/scholarship_form.html', context)

class ScholarshipDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    -> scholarship delete view
    """
    model = Scholarship
    success_url = '/scholarship-dash'

    def test_func(self):
        obj = self.get_object()
        if obj:
            return True
        return False

class ScholarshipAppCreateView(LoginRequiredMixin, CreateView):
    """
    -> scholarship app create view
    """
    model = ScholarshipApp
    success_url = "/users/profile/"
    fields = ['cover', 'confirm']


    def form_valid(self, form):
        #grabbing scholarship primary key
        scholarships = self.kwargs["scholarships"]
        #setting the student and scholarship
        form.instance.student = self.request.user
        form.instance.scholar = Scholarship.objects.all().filter(id=scholarships)[0]
        #determing whether student already applied to scholarship
        match = ScholarshipApp.objects.all().filter(scholar=form.instance.scholar, student=form.instance.student)
        if match:
            messages.warning(self.request,f"You have already applied to this scholarship. Check on the status below.")
            return redirect("users:profile")
        else:
            form.instance.status = "P"
            messages.success(self.request,f"Congrats you have successfullly applied to this scholarship!")
            app_title = form.instance.scholar.title
            send_mail(
                f"Congrats you have successfullly applied {app_title}!", 
                f"Congrats you have successfullly applied {app_title}!", 
                EMAIL_HOST_USER, 
                [form.instance.student.email], 
                fail_silently = False,
                html_message=f"<h1>Thank you for applying to {app_title}!</h1><p>Your application is currently being reviewed. Please <a href='https://www.flairnow.org/users/login'>log in</a> to your profile to view the status of your application. </p>",
            )
            return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super(ScholarshipAppCreateView, self).get_context_data(**kwargs)
        context['scholarship'] = Scholarship.objects.all().filter(id=self.kwargs["scholarships"])[0]
        return context

class ScholarshipApplicants(LoginRequiredMixin, DetailView):
    """
    -> applicants
    """
    model = Scholarship
    template_name = "core/scholarshipapplicants_detail.html"

    def get_context_data(self, **kwargs):
        context = super(ScholarshipApplicants, self).get_context_data(**kwargs)
        context = {
            'object': Scholarship.objects.all().filter(id=self.kwargs["pk"])[0],
            'applicants': ScholarshipApp.objects.all().filter(scholar=self.kwargs["pk"]),
        } 
        return context

class ScholarshipAppDetailView(LoginRequiredMixin, DetailView):
    """
    -> scholarship app detail view
    """
    model = ScholarshipApp

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class ScholarshipAppUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    -> scholarship app update view
    """
    model = ScholarshipApp
    fields = [
        'status', 
        ]
    template_name_suffix = '_org_update_form'

    def form_valid(self, form):
        form.instance.scholar.org = self.request.user
        app = ScholarshipApp.objects.all().filter(id=self.object.id).first()
        messages.success(self.request, f"You have updated the scholarship application.")
        app_title = app.title
        send_mail(
            f"Your Application For {app_title} Has Been Updated!", 
            f"Your Application For {app_title} Has Been Updated!", 
            EMAIL_HOST_USER, 
            [app.student.email], 
            fail_silently = False,
            html_message=f"<h1>Thank you for applying to {app_title}!</h1><p>Your application has been reviewed. Please <a href='https://www.flairnow.org/users/login'>log in</a> to your profile to view the status of your application. </p>",
        )
        return super().form_valid(form)

    def test_func(self):
        obj = self.get_object()
        if obj:
            return True
        return False

class ExternalCreateView(LoginRequiredMixin, CreateView):
    """
    -> external create view
    """
    model = External
    fields = ['host','title','type','field','link']
    success_url = '/external-dash/'


    def form_valid(self, form):
        form.instance.org = self.request.user
        return super().form_valid(form)

class ExternalUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    -> external update view
    """
    model = External
    fields = ['host','title','type','field','link']
    success_url = '/external-dash/'

    def form_valid(self, form):
        form.instance.org = self.request.user
        return super().form_valid(form)

    def test_func(self):
        obj = self.get_object()
        if obj:
            return True
        return False

class ExternalDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    -> external delete view
    """
    model = External
    success_url = '/external-dash/'

    def test_func(self):
        obj = self.get_object()
        if obj:
            return True
        return False