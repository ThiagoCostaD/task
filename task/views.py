from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import FormView, ListView
from django.views.generic.edit import CreateView, UpdateView

from .forms import TaskForm
from .models import Task


class TaskListView(ListView, LoginRequiredMixin):
    model = Task
    template_name = 'task/task_list.html'
    context_name = 'tasks'
    login_url = 'task/login.html'

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Task.objects.none()
        filter_option = self.request.GET.get('all')
        if filter_option == 'completed':
            return Task.objects.filter(user=self.request.user, completed=True)
        elif filter_option == 'pending':
            return Task.objects.filter(user=self.request.user, completed=False)
        else:
            return Task.objects.filter(user=self.request.user)


class CreateTask(LoginRequiredMixin, CreateView):
    model = Task
    template_name = 'task/create_task.html'
    form_class = TaskForm
    success_url = reverse_lazy('task_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class EditTask(LoginRequiredMixin, UpdateView):
    model = Task
    template_name = 'task/edit_task.html'
    form_class = TaskForm
    success_url = reverse_lazy('task_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

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
        return render(
            request,
            'task/edit_task.html',
            {'form': form, 'task': task}
        )


class DeleteTask(LoginRequiredMixin, CreateView):
    model = Task
    template_name = 'task/delete_task.html'
    form_class = TaskForm
    success_url = reverse_lazy('task_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, 'Tarefa excluída com sucesso.')
        return super().form_valid(form)

    def delete_task(request, task_id):
        task = get_object_or_404(Task, id=task_id, user=request.user)
        if request.method == 'POST':
            task.delete()
            messages.success(request, 'Tarefa excluída com sucesso.')
            return redirect('task_list')
        return redirect(request, 'task/delete_task.html', {'task': task})


class LoginView(FormView):
    temaple_name = 'task/login.html'
    form_class = AuthenticationForm

    def form_valid(self, form):
        user = authenticate(
            self.request,
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password']
        )
        if user is not None:
            login(self.request, user)
            messages.success(self.request, 'Logado com sucesso.')
            return redirect('task_list')
        else:
            messages.error(self.request, 'Usuário ou senha inválidos.')
            return redirect('login_view')


class LogoutView(FormView):
    temaple_name = 'task/logout.html'
    form_class = AuthenticationForm

    def form_valid(self, form):
        logout(self.request)
        messages.success(self.request, 'Deslogado com sucesso.')
        return redirect('login_view')


class RegisterView(FormView):
    template_name = 'task/register.html'
    form_class = UserCreationForm

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        messages.success(self.request, 'Usuário criado com sucesso.')
        return redirect('task_list')
