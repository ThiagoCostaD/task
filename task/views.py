from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import get_object_or_404, redirect, render

from .forms import TaskForm
from .models import Task


@login_required
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            messages.success(request, 'Tarefa criada com sucesso.')
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'task/create_task.html', {'form': form})


@login_required
def task_list(request):
    filter_option = request.GET.get('filter', 'all')
    if filter_option == 'completed':
        tasks = Task.objects.filter(user=request.user, completed=True)
        messages.success(request, 'Tarefas concluídas.')
    elif filter_option == 'pending':
        tasks = Task.objects.filter(user=request.user, completed=False)
        messages.success(request, 'Tarefas pendentes.')
    else:
        tasks = Task.objects.filter(user=request.user)
        messages.success(request, 'Todas as tarefas.')

    return render(request, 'task/task_list.html', {'tasks': tasks})


@login_required
def edit_task(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tarefa atualizada com sucesso.')
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'task/edit_task.html', {'form': form, 'task': task})


@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    if request.method == 'POST':
        task.delete()
        messages.success(request, 'Tarefa excluída com sucesso.')
        return redirect('task_list')
    return redirect(request, 'task/delete_task.html', {'task': task})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            if user is not None:
                login(request, user)
                messages.success(request, f'Bem-vindo(a), {user.username}!')
                return redirect('task_list')
            else:
                messages.error(request, 'Usuário ou senha inválidos.')

        else:
            messages.error(request, 'Dados inválidos.')
    else:
        form = AuthenticationForm()
    return render(request, 'task/login.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.success(request, 'Deslogado com sucesso.')
    return redirect('login_view')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Usuário criado com sucesso.')
            return redirect('task_list')
        else:
            messages.error(request, 'Dados inválidos.')
    else:
        form = UserCreationForm()
    return render(request, 'task/register.html', {'form': form})
