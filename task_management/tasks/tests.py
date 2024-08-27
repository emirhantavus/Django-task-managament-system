from django.test import TestCase
from django.contrib.auth import get_user_model
from tasks.models import Task
from projects.models import Project

User = get_user_model()

class TaskTestCase(TestCase):
      def setUp(self):
            self.user = User.objects.create_user(email='testuser@example.com', password='password123')
            self.project = Project.objects.create(name='Test Project', description='Test project description')

      def test_task_creation(self):
            task = Task.objects.create(
                  project = self.project,
                  user = self.user,
                  title = "task1",
                  description = "description1"
            )
            self.assertEqual(task.title,'task1')
            self.assertEqual(task.project.name,'project1')
            self.assertEqual(task.user.email,'user1@mail.com')
            self.assertFalse(self.completed)
      
      def test_task_str_method(self):
            self.assertEqual(str(self.task),"Task1")