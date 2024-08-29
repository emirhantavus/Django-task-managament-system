from tasks.models import Task

class TaskRepository:
      
      @staticmethod
      def get_tasks_by_user(user):
            return Task.objects.filter(user=user)
      
      @staticmethod
      def get_tasks_by_id(task_id):
            return Task.objects.filter(id=task_id)
      
      @staticmethod
      def delete_task(task_id):
            task = Task.objects.get(id=task_id)
            task.delete()
            