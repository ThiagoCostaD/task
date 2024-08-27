from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

base_name = 'task'

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path(
        'create/',
        views.create_task,
        name='create_task'
    ),
    path(
        'edit/<int:task_id>/',
        views.edit_task,
        name='edit_task'
    ),
    path(
        'delete/<int:task_id>/',
        views.delete_task,
        name='delete_task'
    ),
    path(
        'login/',
        auth_views.LoginView.as_view(template_name='task/login.html'),
        name='login'
    ),
    path(
        'logout/',
        auth_views.LogoutView.as_view(),
        name='logout'
    ),
    path(
        'register/',
        views.register,
        name='register'
    ),
]
