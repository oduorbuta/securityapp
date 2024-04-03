from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import User


def login_view(request):
     if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Find user by username
        user = User.objects.filter(username=username).first()
        if user and user.password == password:
            # Authentication successful, redirect to home page
            return render(request,'home.html')
        else:
            # Invalid login credentials
            return render(request, 'login.html', {'error': 'Invalid email or password'})
     return render(request, 'login.html')

def register_view(request):
     if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if password != confirm_password:
            # Passwords don't match
            return render(request, 'register.html', {'error': 'Passwords do not match'})
        # Create a new user
        User.objects.create(username=username, password=password)
        # Redirect to login page or any other page
        return redirect('login')
     return render(request, 'register.html')

def home_view(request):
    # Check if user is authenticated
    if request.user.is_authenticated:
        return render(request, 'home.html')
    else:
        # Redirect to login page if user is not authenticated
        return redirect('login')
