import os
from datetime import datetime as dt
from datetime import timedelta

from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
from dotenv import load_dotenv


from .models import Task, User


load_dotenv()
email = os.getenv('Email')


def check_task_time():

    """
    Function check if tasks overdue or coming soon then send emails to
    users with notification
    """
    users = User.objects.all()
    for user in users:
        tasks = user.task.filter(is_done=False)
        for task in tasks:
            if task.due_date:
                result_coming_soon, result_overdue = timedelta(8), timedelta(0)

                if (task.due_date.replace(tzinfo=None) - dt.now() <
                        result_overdue):
                    Task.objects.filter(pk=task.id).update(
                        delayed_task=True,
                        coming_soon_task=True
                    )
                    send_message(task.user, task)
                    continue

                if (task.due_date.replace(tzinfo=None) - dt.now() <
                        result_coming_soon):
                    Task.objects.filter(pk=task.id).update(
                        coming_soon_task=True
                    )
                    send_message(task.user, task)


def send_message(user, task):
    user = get_object_or_404(User, pk=user)
    if not task.delayed_task:
        send_mail(
            f'Task manager',
            f'Hello {user.name} \n'
            f'Your task {task.topic} is coming soon, please do not forget to'
            f'solve this task ',
            email,
            [user.email],
            fail_silently=False,
        )
    else:
        send_mail(
            f'Task manager',
            f'Hello {user.name} \n'
            f'Your task {task.topic} is overdue, please do not forget to',
            email,
            [user.email],
            fail_silently=False,
        )
