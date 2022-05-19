from datetime import datetime as dt
from datetime import timedelta

from .models import Category, Task, User


def filter_task_list(request, parameter):
    if parameter == 'all_task':
        tasks_list = Task.objects.filter(is_done=False,
                                         author=request.user).select_related(
            'category'
        )

    elif parameter == 'task_done':
        tasks_list = Task.objects.filter(is_done=True,
                                         author=request.user).select_related(
            'category'
        )
    elif parameter == 'coming_soon':
        tasks_list = Task.objects.filter(coming_soon_task=True,
                                         author=request.user
                                         ).select_related(
            'category'
        )
    elif parameter == 'delayed_task':
        tasks_list = Task.objects.filter(delayed_task=True,
                                         author=request.user).select_related(
            'category'
        )

    categories = Category.objects.filter(author=request.user)
    data = {
        'tasks': tasks_list,
        'tasks_page': True,
        'categories': categories
    }
    return data


def check_task_time():
    users = User.objects.all()
    for user in users:
        tasks = user.task.all()
        for task in tasks:
            if task.due_date:
                result_coming_soon = timedelta(8)
                result_overdue = timedelta(0)
                if (task.due_date.replace(tzinfo=None) - dt.now() <
                        result_coming_soon):
                    Task.objects.filter(pk=task.id).update(
                        coming_soon_task=True)
                if (task.due_date.replace(tzinfo=None) - dt.now() <
                        result_overdue):
                    Task.objects.filter(pk=task.id).update(
                        delayed_task=True, coming_soon_task=False)
