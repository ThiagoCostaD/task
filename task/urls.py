from django.contrib.auth import views as auth_views
from django.urls import path

from .views import CreateTask, DeleteTask, EditTask, RegisterView, TaskListView

base_name = 'task'

urlpatterns = [
    path(
        '',
        TaskListView.as_view(),
        name='task_list'
    ),
    path(
        'create/',
        CreateTask.as_view(),
        name='create_task'
    ),
    path(
        'edit/<int:task_id>/',
        EditTask.as_view(),
        name='edit_task'
    ),
    path(
        'delete/<int:task_id>/',
        DeleteTask.as_view(),
        name='delete_task'
    ),
    path(
        'login/',
        auth_views.LoginView.as_view(
            template_name='task/login.html'
        ),
        name='login'
    ),
    path(
        'logout/',
        auth_views.LogoutView.as_view(),
        name='logout'
    ),
    path(
        'register/',
        RegisterView.as_view(),
        name='register'
    ),
]
