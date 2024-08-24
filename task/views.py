from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .models import Task


def login(request):
    return render(request, 'registration/login.html')


def create_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        due_date = request.POST.get('due_date')
        task = Task(title=title, description=description,
                    due_date=due_date, user=request.user)
        task.save()
        return redirect('tasks:list')
    return render(request, 'tasks/create.html')


def edit_task(request, pk):
    task = get_object_or_404(Task, id=pk)
    if request.method == 'POST':
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.due_date = request.POST.get('due_date')
        task.save()
        return redirect('tasks:list')
    return render(request, 'tasks/edit.html', {'task': task})


@login_required
def list_tasks(request):
    if request.user.is_authenticated:
        tasks = Task.objects.filter(user=request.user)
        return render(request, 'task/list.html', {'tasks': tasks})
    else:

        return redirect('login')


def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('tasks:list')
