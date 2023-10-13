from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from .models import CustomUser
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from .forms import RegistrationForm, LoginForm, LogoutForm


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            role = form.cleaned_data['role']

            # Перевірка, чи користувач з таким email-ом вже існує
            if CustomUser.objects.filter(email=email).exists():
                messages.error(request, 'User with this email already exists.')
            else:
                user = CustomUser.create(email, password, first_name, last_name, role)
                if user:
                    user = authenticate(request, email=email, password=password)
                    if user:
                        login(request, user)
                        messages.success(request, 'Registration successful!')
                        return redirect('home')
        else:
            messages.error(request, 'Registration failed. Please check the provided information.')
    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():  
           email = form.cleaned_data['email']
           password = form.cleaned_data['password']
           
           user = authenticate(request, email=email, password=password)
           
           if user is not None:
                login(request, user)
                return redirect('/book/') 
                
        #    else:
        #     messages.error(request, 'User is not register, please register accaunt!')
    else:
        form = LoginForm()
    
    return render(request, 'login.html', {'form': form })



def user_logout(request):
    if request.method == 'POST':
        form = LogoutForm(request.POST)
        if form.is_valid():
            # Виконуємо вихід користувача
            logout(request)
            return redirect('login')  
    else:
        form = LoginForm()
    
    return render(request, 'logout_template.html', {'form': form})



def show_all_users(request):
    users = CustomUser.objects.all()
    return render(request, 'list_all_users.html', {'users': users })
    

def views_user(request, user_id):
    user = get_object_or_404(CustomUser, pk=user_id)
    return render(request, 'views_user.html', {'user': user})
