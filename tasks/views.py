from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import (TemplateView, View, ListView, CreateView,
                                  UpdateView)

from .forms import CategoryForm, TaskForm
from .models import Category, Task


class IndexView(TemplateView):
    """ Start page."""

    template_name = 'tasks/index.html'


class TasksListView(ListView):
    """ List of all running tasks."""

    model = Task
    template_name = 'tasks/tasks_list.html'
    context_object_name = 'tasks'
    queryset = Task.objects.filter(is_done=False).select_related('category')


class CategoryDetailView(ListView):
    """Tasks list filtered by category."""

    model = Category
    template_name = 'tasks/task_by_category.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        category = get_object_or_404(Category, slug=self.kwargs['slug'])
        return category.task.filter(author=self.request.user)


class TaskDetailView(ListView):
    """ Full task description."""

    model = Task
    template_name = 'tasks/direct_task.html'
    context_object_name = 'task'

    def get_queryset(self):
        return Task.objects.get(pk=self.kwargs['task_id'])


class TaskUpdateView(UpdateView):
    """Update task."""

    form_class = TaskForm
    template_name = 'tasks/create_task.html'
    success_url = reverse_lazy('tasks:task_list')

    def get_object(self, queryset=None):
        return Task.objects.get(pk=self.kwargs['task_id'])


class TaskDoneView(View):
    """Change task status to done."""

    def get(self, request, task_id):
        Task.objects.filter(pk=task_id).update(is_done=True)
        return redirect('tasks:task_list')


class CreatTaskView(CreateView):
    """Create new task."""

    form_class = TaskForm
    template_name = 'tasks/create_task.html'
    success_url = reverse_lazy('tasks:task_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class CreatCategoryView(CreateView):
    """Create new category."""

    form_class = CategoryForm
    template_name = 'tasks/create_category.html'
    success_url = reverse_lazy('tasks:task_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TaskFilterView(ListView):
    """Filter task."""

    model = Task
    template_name = 'tasks/tasks_list.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        task = Task.objects.filter(author=self.request.user).filter(
            Q(is_done=self.request.GET.get('done', False)) |
            Q(coming_soon_task=self.request.GET.get('soon', False)) |
            Q(is_done=self.request.GET.get('all_task', False))
        )
        return task
