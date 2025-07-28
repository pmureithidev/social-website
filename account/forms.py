from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from .models import Profile

# login form
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

# registartion form
class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = get_user_model()
        fields = ['username', 'first_name', 'email']

    # validation to check if the passwords match
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("Passwords don't match.")
        return cd['password2']
    
    # prevent users from using an existing email during registration
    def clean_email(self):
        data = self.cleaned_data['email']
        if User.objects.filter(email=data).exists():
            raise forms.ValidationError('Email a;ready in use.')
        return data

class UserEditForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'email']
    def clean_email(self):
        data = self.cleaned_data['email']
        qs = User.objects.exclude(id=self.instance.id).filter(email=data)

        if qs.exists():
            raise forms.ValidationError('Email already in use.')
        return data
    
class ProfileEditForm(forms.ModelForm):
        class Meta:
            model = Profile
            fields = ['date_of_birth', 'photo']
    
    
