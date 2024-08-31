from django.db.models.signals import post_save
from django.dispatch import receiver
from tasks.models import Task
from .tasks import send_task_notification

@receiver(post_save, sender=Task)
def task_completed(sender, instance, **kwargs):
    if instance.completed:
        send_task_notification.delay(instance.id)
