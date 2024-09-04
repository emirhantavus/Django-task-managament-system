from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'task_management.settings')

app = Celery('task_management')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'check_task_deadlines': {
        'task': 'tasks.check_task_deadlines',
        'schedule': crontab(minute=0, hour='*/1'),
    },
}

app.autodiscover_tasks()
