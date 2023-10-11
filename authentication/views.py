from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from .models import CustomUser
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.hashers import check_password


def register(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        role = request.POST['role']

        # Створення користувача на основі введених даних
        user = CustomUser.create(email, password, first_name, last_name, role)
        if user:
            # Вхід користувача після реєстрації
            user = authenticate(request, email=email, password=password)
            if user:
                login(request, user)
                messages.success(request, 'Registration successful!')
                return redirect('home')  # Перенаправлення на головну сторінку
    return render(request, 'register.html')




def user_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        try:
            user = CustomUser.objects.get(email=email)
            print(user)
            print(type(str(user)))
            print(type(password))

            print(password)
            print(password==str(user))

            if str(user) == password:
                login(request, user)
                return redirect('/book/')

        except ValueError:
            print(123)


    return render(request, 'login.html')


def user_logout(request):
    logout(request)
    return redirect('login') 

def show_all_users(request):
    users = CustomUser.objects.all()
    return render(request, 'list_all_users.html', {'users': users })
    

def views_user(request, user_id):
    user = get_object_or_404(CustomUser, pk=user_id)
    return render(request, 'views_user.html', {'user': user})
