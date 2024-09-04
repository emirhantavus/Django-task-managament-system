from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from tasks.models import Task
from django.utils import timezone
from datetime import timedelta

@shared_task
def send_task_notification(task_id):
      try:
            task = Task.objects.get(id=task_id)
            subject = f"Task '{task.title}' completed"
            message = f"{task.user.email}, \n Task '{task.title}' in project {task.project.name} is completed"
            user_message_list = [task.user.email]
            send_mail(subject,message,'whisber1@gmail.com',user_message_list,fail_silently=False)
      except Task.DoesNotExist:
            return 'task does not exist'
      return f"Notification sent for task : {task.title}"

@shared_task
def check_task_deadlines():
      deadline_task = Task.objects.filter(deadline = timezone.now() + timedelta(hours=24),completed=False)
      for task in deadline_task:
            for users in task.user.all():
                  send_mail(
                        subject=f"upcoming task : {task.title}",
                        message = f"Heyy, {task.title} task is due on {task.deadline}. More attention !!!",
                        from_email= 'test@mail.com',
                        recipient_list=[users.email]
                  )
      return "test"