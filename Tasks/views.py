from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request, 'home.html')


def signup(request):
    if (request.method == "POST"):
        if (request.POST['password1'] == request.POST['password2']):
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                print(user)
                user.save()
                return HttpResponse("User created successfully")
            except:
                return render(request, 'signup.html', {'form': UserCreationForm, 'error': 'User already exists'})
        else:
            return render(request, 'signup.html', {'form': UserCreationForm, 'error': "Password don't match"})
    else:
        return render(request, 'signup.html', {'form': UserCreationForm})
