from django.contrib.auth import views as auth_views
from django.urls import include, path

from .views.api import (CreateTaskViewSet, DeleteTaskViewSet, EditTaskViewSet,
                        LoginViewSet, LogoutViewSet, RegisterViewSet,
                        TaskViewSet)
from .views.site import (CreateTask, DeleteTask, EditTask, RegisterView,
                         TaskListView)

base_name = 'task'

urlpatterns = [
    path(
        'api-auth/',
        include('rest_framework.urls', namespace='rest_framework')
    ),
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
        'edit/<int:pk>/',
        EditTask.as_view(),
        name='edit_task'
    ),
    path(
        'delete/<int:pk>/',
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
    path(
        'api/task/',
        TaskViewSet.as_view(),
        name='api_task'
    ),
    path(
        'api/create/',
        CreateTaskViewSet.as_view({'post': 'create'}),
        name='api_create_task'
    ),
    path(
        'api/edit/<int:pk>/',
        EditTaskViewSet.as_view({'put': 'update'}),
        name='api_edit_task'
    ),
    path(
        'api/delete/<int:pk>/',
        DeleteTaskViewSet.as_view({'delete': 'destroy'}),
        name='api_delete_task'
    ),
    path(
        'api/login/',
        LoginViewSet.as_view({'get': 'login'}),
        name='api_login'
    ),
    path(
        'api/logout/',
        LogoutViewSet.as_view({'get': 'logout'}),
        name='api_logout'
    ),
    path(
        'api/register/',
        RegisterViewSet.as_view({'post': 'create'}),
        name='api_register'
    ),
]
