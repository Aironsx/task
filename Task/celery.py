from __future__ import absolute_import, unicode_literals

import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Task.settings')

app = Celery('Task')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'check_task_status_every_minute': {
        'task': 'tasks.tasks.check_time',
        'schedule': crontab(),

    },
}
