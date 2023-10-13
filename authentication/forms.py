from django import forms
from django.contrib.auth.models import User
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError
import re 
from django.contrib import messages 

# def validate_email(value):
#     pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
#     if not pattern.fullmatch(value):
#         raise forms.ValidationError('Email not valid')

def validate_password(value):
    pattern = re.compile(r'^(?=.*[A-Za-z])(?=.*\d).+')
    if not pattern.fullmatch(value):
        raise forms.ValidationError('Password is not valid')
   

class RegistrationForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput, validators=[validate_password])
    first_name = forms.CharField()
    last_name = forms.CharField()
    role = forms.ChoiceField(choices=[('user', 'User'), ('admin', 'Admin')])
    
    

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    
    
class LogoutForm(forms.Form):
    pass
    
    

    
    

    

    
    


