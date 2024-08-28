from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import DeleteView, FormView, ListView
from django.views.generic.edit import CreateView, UpdateView

from .forms import TaskForm
from .models import Task


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'task/task_list.html'
    context_object_name = 'tasks'
    login_url = 'task/login.html'

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Task.objects.none()
        filter_option = self.request.GET.get(
            'filter', 'all')
        if filter_option == 'completed':
            return Task.objects.filter(user=self.request.user, completed=True)
        elif filter_option == 'pending':
            return Task.objects.filter(user=self.request.user, completed=False)
        else:
            return Task.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter_option'] = self.request.GET.get(
            'filter', 'all')
        return context


class CreateTask(LoginRequiredMixin, CreateView):
    model = Task
    template_name = 'task/create_task.html'
    form_class = TaskForm
    success_url = reverse_lazy('task_list')

    def form_valid(self, form):
        task = form.save(commit=False)
        task.user = self.request.user
        task.save()
        return super().form_valid(form)


class EditTask(LoginRequiredMixin, UpdateView):
    model = Task
    template_name = 'task/edit_task.html'
    form_class = TaskForm
    success_url = reverse_lazy('task_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, 'Tarefa atualizada com sucesso.')
        return super().form_valid(form)

    def get_object(self, queryset=None):
        """ Garante que apenas o dono da tarefa possa editá-la """
        obj = super().get_object()
        if not obj.user == self.request.user:
            raise Http404
        return obj


class DeleteTask(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'task/delete_task.html'
    success_url = reverse_lazy('task_list')

    def get_object(self, queryset=None):
        object = super().get_object()
        if not object.user == self.request.user:
            raise Http404
        return object

    def delete(self, request, *args, **kwargs):

        response = super().delete(request, *args, **kwargs)
        messages.success(self.request, 'Tarefa excluída com sucesso.')
        return response


class LoginView(FormView):
    template_name = 'task/login.html'
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
    template_name = 'task/logout.html'
    form_class = AuthenticationForm

    def form_valid(self, form):
        logout(self.request)
        messages.success(self.request, 'Deslogado com sucesso.')
        return redirect('login_view')


class RegisterView(FormView):
    template_name = 'task/register.html'
    form_class = UserCreationForm
    # Redirect after successful registration
    success_url = reverse_lazy('task_list')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        messages.success(self.request, 'Usuário criado com sucesso.')
        return redirect(self.success_url)
