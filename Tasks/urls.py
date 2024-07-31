from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="tasksHome"),
    path('sign_up/', views.sign_up, name="tasksSignup"),
    path('tasks/', views.tasks, name="tasksTasks"),
    path('log_out/', views.log_out, name="tasksLogout"),
    path('log_in/', views.log_in, name="tasksLogin"),
    path('tasks/create/', views.createTask, name="tasksCreateTask"),
    path('tasks/<int:taskId>/', views.taskDetails, name="tasksTaskDetails"),
    path('tasks/update/<int:taskId>/', views.updateTask, name="tasksUpdateTask"),
    path('tasks/complete/<int:taskId>/',
         views.completeTask, name="tasksCompleteTask"),
    path('tasks/delete/<int:taskId>/', views.deleteTask, name="tasksDeleteTask"),
    path('tasks/completed/', views.completedTasksList,
         name="tasksCompletedTasksList"),
    path('tasks/pending/', views.pendingTasksList,
         name="tasksPendingTasksList"),
]
