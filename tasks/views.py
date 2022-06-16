from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import (DeleteView, ListView, TemplateView,
                                  UpdateView, View)

from .forms import CategoryForm, TaskForm
from .mixin import ObjectCreateMixin
from .models import Category, Task


class IndexView(TemplateView):
    """ Start page."""

    template_name = 'tasks/index.html'


class TasksListView(ListView):
    """ List of all running tasks."""

    model = Task
    template_name = 'tasks/tasks_list.html'
    context_object_name = 'tasks'
    queryset = Task.objects.filter(is_done=False).select_related(
        'category')[::-1]


class CategoryDetailView(ListView):
    """Tasks list filtered by category."""

    model = Category
    template_name = 'tasks/task_by_category.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        return Task.objects.filter(author=self.request.user).select_related(
            'category').filter(category__slug__iexact=self.kwargs['slug'],
                               )[::-1]


class TaskDetailView(ListView):
    """ Full task description."""

    model = Task
    template_name = 'tasks/direct_task.html'
    context_object_name = 'task'

    def get_queryset(self):
        return get_object_or_404(Task, slug=self.kwargs['slug'])


class TaskUpdateView(UpdateView):
    """Update task."""

    form_class = TaskForm
    template_name = 'tasks/create_task.html'
    success_url = reverse_lazy('tasks:task_list')

    def get_object(self, queryset=None):
        return Task.objects.get(slug=self.kwargs['slug'])

    def get_success_url(self):
        return reverse_lazy(
            'tasks:task_list',
            kwargs={'username': self.request.user.username}
        )

    def get_context_data(self, **kwargs):
        context = super(TaskUpdateView, self).get_context_data(**kwargs)
        context['is_edit'] = 'is_edit'
        return context


class TaskDoneView(View):
    """Change task status to done."""

    def get(self, request, slug):
        Task.objects.filter(slug=slug).update(is_done=True)
        return redirect('tasks:task_list', username=self.request.user.username)


class CreatTaskView(ObjectCreateMixin):
    """Create new task."""

    form_class = TaskForm
    template_name = 'tasks/create_task.html'


class CreatCategoryView(ObjectCreateMixin):
    """Create new category."""

    form_class = CategoryForm
    template_name = 'tasks/create_category.html'


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


class TaskDeleteView(DeleteView):
    """ Delete task."""

    model = Task
    template_name = 'tasks/confirm_task_delete.html'

    def get_success_url(self):
        return reverse_lazy(
            'tasks:task_list',
            kwargs={'username': self.request.user.username}
        )


class CategoriesListView(ListView):
    """Categories list."""

    model = Category
    template_name = 'tasks/categories_list.html'
    context_object_name = 'categories'

    def get_queryset(self):
        return Category.objects.filter(author=self.request.user)


class CategoryDeleteView(DeleteView):
    model = Category

    def get_success_url(self):
        return reverse_lazy(
            'tasks:task_list',
            kwargs={'username': self.request.user.username}
        )
