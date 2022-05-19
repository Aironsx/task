from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from .forms import CategoryForm, TaskForm
from .models import Category, Task


def index(request):
    return render(request, 'tasks/index.html')


@login_required
def tasks(request):
    tasks = Task.objects.filter(is_done=False).select_related('category')
    context = {
        'tasks':tasks
    }
    return render(request, 'tasks/tasks_list.html', context)


@login_required
def category_task(request, slug):
    category = get_object_or_404(Category, slug=slug)
    tasks = category.task.filter(author=request.user)
    context = {
        'category': category,
        'tasks': tasks,
    }
    return render(request, 'tasks/task_by_category.html', context)


@login_required
def task(request, task_id):
    task = Task.objects.get(pk=task_id)
    context = {
        'task': task
    }
    return render(request, 'tasks/direct_task.html', context)


@login_required
def edit_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    if request.user != task.author:
        return redirect(task)
    is_edit = True
    form = TaskForm(
        request.POST or None,
        instance=task,
    )
    context = {
        'form': form,
        'is_edit': is_edit
    }
    if form.is_valid():
        form.save()
        return redirect(task)
    return render(request, 'tasks/create_task.html', context)


def task_done(request, task_id):
    Task.objects.filter(pk=task_id).update(is_done=True)
    return redirect('tasks:task_list', param='all_task')


@login_required
def create_task(request):
    form = TaskForm(request.POST or None)
    if form.is_valid():
        task = form.save(commit=False)
        task.author = request.user
        task.save()
        return redirect('tasks:task_list', param='all_task')
    context = {
        'form': form,
    }
    return render(request, 'tasks/create_task.html', context)


@login_required
def create_category(request):
    form = CategoryForm(request.POST or None)
    if form.is_valid():
        category = form.save(commit=False)

        category.author = request.user
        category.save()
        return redirect('tasks:task_list', param='all_task')
    context = {
        'form': form,
    }
    return render(request, 'tasks/create_category.html', context)


def filter_tasks(request):
    task = Task.objects.filter(
        Q(is_done=request.GET.get('q', False))|
        Q(coming_soon_task=request.GET.get('s', False))|
        Q(is_done=request.GET.get('all_task', False))
    )
    return render(request, 'tasks/tasks_list.html', {'tasks': task})
