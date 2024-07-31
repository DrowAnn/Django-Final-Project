from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="tasksHome"),
    path('sign_up/', views.sign_up, name="tasksSignup"),
    path('tasks/', views.tasks, name="tasksTasks"),
    path('log_out/', views.log_out, name="tasksLogout"),
    path('log_in/', views.log_in, name="tasksLogin"),
    path('tasks/create/', views.createTask, name="tasksCreateTask")
]
