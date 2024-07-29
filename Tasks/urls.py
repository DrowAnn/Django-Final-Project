from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "tasksHome"),
    path('signup/', views.signup, name = "tasksSignup"),
]