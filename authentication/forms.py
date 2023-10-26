from django import forms
from django.contrib.auth.models import User
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError
import re 
from django.contrib import messages 
from authentication.models import CustomUser, CustomUserManager


def validate_password(value):
    pattern = re.compile(r'^(?=.*[A-Za-z])(?=.*\d).+')
    if not pattern.fullmatch(value):
        raise forms.ValidationError('Password is not valid')
   



   
class RegistrationForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'middle_name', 'email', 'password', 'role']    

class LoginForm(forms.Form):
    email = forms.EmailField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput, validators=[validate_password])

    
    
class LogoutForm(forms.Form):
    pass
    
    

    
    

    

    
    


