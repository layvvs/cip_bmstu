from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm


def login_view(request: HttpRequest):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect('/')
        return render(request, 'authapp/login.html')
    email = request.POST["email"]
    password = request.POST["password"]
    user = authenticate(request, username=email, password=password)
    if user:
        login(request, user)
        return redirect('/')
    
    return render(request, "authapp/login.html", {"error": "Invalid login credentials"})

def logout_view(request: HttpRequest):
    logout(request)
    return redirect('/')

def signup_view(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    
    context = {'form': form}
    return render(request, 'authapp/signup.html', context)
