from django.db import models
from projects.models import Project
from django.contrib.auth import get_user_model

User = get_user_model()


class Task(models.Model):
      project = models.ForeignKey(Project,related_name='tasks',on_delete=models.CASCADE)
      user = models.ManyToManyField(User,related_name='tasks')
      title = models.CharField(max_length=255)
      description = models.TextField(blank=True)
      completed = models.BooleanField(default=False)
      deadline = models.DateTimeField(null=True, blank=True)
      
      def complete_task(self):
            self.completed = True
            self.save()
            from .tasks import send_task_notification
            send_task_notification.delay(self.id)
      
      def __str__(self):
            return self.title