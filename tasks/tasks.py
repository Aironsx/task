from celery import shared_task

from .service import check_task_time


@shared_task
def check_time():
    check_task_time()

