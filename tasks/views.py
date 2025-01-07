from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView, CreateView, UpdateView, View, DeleteView
from .models import Task
from .forms import TaskForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy



class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'tasks/list.html'
    context_object_name = 'tasks'
    
    def get_queryset(self):
        user = self.request.user
        search = self.request.GET.get('search', '')
        filter_status = self.request.GET.get('filter', '')

       
        tasks = Task.objects.filter(user=user).order_by('-created_at')

        if search:
            tasks = tasks.filter(title__icontains=search)

        if filter_status:
            tasks = tasks.filter(completed=filter_status)

        paginator = Paginator(tasks, 5)
        page = self.request.GET.get('page')
        tasks = paginator.get_page(page)

        return tasks


class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'tasks/task.html'
    context_object_name = 'task'


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/add_task.html'
    success_url = '/'
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.completed = 'doing'
        messages.success(self.request, "Tarefa criada!")
        return super().form_valid(form)


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/edit_task.html'
    success_url = '/' 
    


class TaskStatusChangeView(LoginRequiredMixin, View):
    def get(self, request, pk):
        task = get_object_or_404(Task, pk=pk, user=request.user)
        
        if task.completed == 'doing':
            task.completed = 'done'
        else:
            task.completed = 'doing'
        task.save()
        return redirect('task-list')


class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy('task-list')
    

    def post(self, request, *args, **kwargs):
        messages.success(request, "Tarefa excluída com sucesso!")
        return super().post(request, *args, **kwargs)
    
    
        

