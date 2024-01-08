# authentication/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import LoginForm, RegistrationForm


def register(request):
    return render(request, 'authentication/register.html')
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('submit_paper')  
    else:
        form = LoginForm()
    return render(request, 'authentication/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')  # Change 'login' to the name of your login page URL

def user_registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()

            # You can add additional logic here to save user profile information
            # For example: UserProfile.objects.create(user=user)

            login(request, user)
            return redirect('home')  # Change 'home' to the name of your home page URL
    else:
        form = RegistrationForm()
    return render(request, 'authentication/register.html', {'form': form})
