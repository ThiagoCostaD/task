from django.urls import path

from . import views

app_name = 'tasks'

urlpatterns = [
    path('', views.list_tasks, name='list'),
    path('login/', views.login, name='login'),
    path('create/', views.create_task, name='create'),
    path('edit/<int:pk>/', views.edit_task, name='edit'),
    path('delete/<int:task_id>/', views.delete_task, name='delete'),
]
