from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from tasks.models import Task

@shared_task
def send_task_notification(task_id):
      try:
            task = Task.objects.get(id=task_id)
            subject = f"Task '{task.title}' completed"
            message = f"{task.user.email}, \n Task '{task.title}' in project {task.project.name} is completed"
            user_message_list = [task.user.email]
            send_mail(subject,message,settings.DEFAULT_FROM_EMAIL,user_message_list)
      except Task.DoesNotExist:
            return 'task does not exist'
      
      return f"Notification sent for task : {task.title}"