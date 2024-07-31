from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect
from .forms import createTaskForm
from .models import Task
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.decorators import login_required

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


@login_required
def log_out(request):
    logout(request)
    return redirect('tasksHome')


@login_required
def tasks(request):
    tasksList = Task.objects.filter(user=request.user)
    return render(request, 'tasks.html', {'tasks': tasksList})


@login_required
def createTask(request):
    if (request.method == "POST"):
        try:
            form = createTaskForm(request.POST)
            newTask = form.save(commit=False)
            newTask.user = request.user
            newTask.save()
            return redirect('tasksTasks')
        except:
            return render(request, 'createTask.html', {'form': createTaskForm, 'error': 'Please provide valid data'})
    else:
        return render(request, 'createTask.html', {'form': createTaskForm})


@login_required
def taskDetails(request, taskId):
    task = get_object_or_404(Task, pk=taskId, user=request.user)
    return render(request, 'taskDetails.html', {'task': task})


@login_required
def updateTask(request, taskId):
    if (request.method == 'POST'):
        try:
            task = get_object_or_404(Task, pk=taskId, user=request.user)
            form = createTaskForm(request.POST, instance=task)
            form.save()
            return redirect('tasksTasks')
        except:
            task = get_object_or_404(Task, pk=taskId, user=request.user)
            form = createTaskForm(instance=task)
            return render(request, 'updateTask.html', {'form': form, 'error': 'Please provide valid data'})
    else:
        task = get_object_or_404(Task, pk=taskId, user=request.user)
        form = createTaskForm(instance=task)
        return render(request, 'updateTask.html', {'form': form})


@login_required
def completeTask(request, taskId):
    if (request.method == "POST"):
        task = get_object_or_404(Task, pk=taskId, user=request.user)
        task.completed = True
        task.completedDate = timezone.now()
        task.save()
        return HttpResponseRedirect(reverse('tasksTaskDetails', kwargs={'taskId': taskId}))
    else:
        return redirect('tasksTasks')


@login_required
def deleteTask(request, taskId):
    if (request.method == "POST"):
        task = get_object_or_404(Task, pk=taskId, user=request.user)
        task.delete()
        return redirect('tasksTasks')
    else:
        return redirect('tasksTasks')


@login_required
def completedTasksList(request):
    tasksList = Task.objects.filter(user=request.user, completed=True)
    return render(request, 'tasks.html', {'tasks': tasksList})


@login_required
def pendingTasksList(request):
    tasksList = Task.objects.filter(user=request.user, completed=False)
    return render(request, 'tasks.html', {'tasks': tasksList})
