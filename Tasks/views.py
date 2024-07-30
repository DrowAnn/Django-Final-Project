from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request, 'home.html')


def sign_up(request):
    if (request.method == "POST"):
        if (request.POST['password1'] == request.POST['password2']):
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                print(user)
                user.save()
                login(request, user)
                return redirect('tasksTasks')
            except:
                return render(request, 'signup.html', {'form': UserCreationForm, 'error': 'User already exists'})
        else:
            return render(request, 'signup.html', {'form': UserCreationForm, 'error': "Password don't match"})
    else:
        return render(request, 'signup.html', {'form': UserCreationForm})


def log_in(request):
    if (request.method == "POST"):
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if (user is None):
            return render(request, 'login.html', {'form': AuthenticationForm, 'error': "User or Password is incorrect"})
        else:
            login(request, user)
            return redirect('tasksTasks')
    else:
        return render(request, 'login.html', {'form': AuthenticationForm})


def log_out(request):
    logout(request)
    return redirect('tasksHome')


def tasks(request):
    return render(request, 'tasks.html')
