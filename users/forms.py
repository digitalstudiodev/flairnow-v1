from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from .models import Profile, User, Contact
from bootstrap_datepicker_plus import DatePickerInput

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=60)
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']
    
    def save(self, commit=True):
        user = super().save(commit=commit)
        user.is_student = True
        user.is_organization = False
        user.is_approved = True
        if commit:
            user.save()
        return user

class OrgRegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=60)
    
    class Meta:
        model = User
        fields = ['org_name', 'email', 'password1', 'password2']
    
    def save(self, commit=True):
        user = super().save(commit=commit)
        user.is_student = False
        user.is_organization = True
        user.is_approved = False
        if commit:
            user.save()
        return user

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

class LoginForm(forms.ModelForm):
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'password']

    def clean(self):
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']
        if not authenticate(email=email, password=password):
            raise forms.ValidationError("Invalid Login")

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = [
            'phone', 'dob', 'street', 'apt',
            'zip_code', 'city', 'state', 'linkedin'
        ]
        widgets = {
            'dob': DatePickerInput(format='%Y-%m-%d'), 
        }