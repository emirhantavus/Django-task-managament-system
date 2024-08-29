from tasks.models import Task
from projects.models import Project
from django.contrib.auth import get_user_model

User = get_user_model()

class TaskService:
      @staticmethod
      def create_task(user_email,project_name,task_title,task_description):
            try:
                  user = User.objects.get(email=user_email)
                  project = Project.objects.get(name=project_name)
                  task = Task(user = user,project=project,title = task_title,description=task_description)
                  task.save()
                  return task
            except user.DoesNotExist:
                  raise ValueError("user does not exist")
            except project.DoesNotExist:
                  raise ValueError("project  does not exist")
            
      @staticmethod
      def complete_task(task_id):
            try:
                  task = Task.objects.get(id=task_id)
                  task.completed = True
                  task.save()
                  return task
            except task.DoesNotExist:
                  raise ValueError("task does not exist")