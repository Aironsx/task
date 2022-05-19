from datetime import datetime as dt
from datetime import timedelta

from .models import Task, User


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
