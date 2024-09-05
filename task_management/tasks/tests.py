from django.test import TestCase
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from tasks.models import Task
from projects.models import Project
from django.conf import settings

User = get_user_model()

class TaskTestCase(TestCase):
      def setUp(self):
            self.user1 = User.objects.create_user(email='user1@mail.com', password='123456')
            self.user2 = User.objects.create_user(email='user2@mail.com', password='123456')
            self.project = Project.objects.create(name='project1', description='desc1')
            self.task = Task.objects.create(
                project=self.project,
                title='task',
                description='desc1',
                completed=False
            )
            self.task.user.set([self.user1, self.user2])

      def test_task_creation(self):
            task = Task.objects.create(
                project=self.project,
                title="task1",
                description="description1"
            )
            task.user.set([self.user1])
            self.assertEqual(task.title, 'task1')
            self.assertEqual(task.project.name, 'project1')
            self.assertIn(self.user1, task.user.all())

      def test_task_str_method(self):
            self.assertEqual(str(self.task), "task")
            
      def test_task_exists(self):
            self.assertEqual(self.task.title, 'task')
            self.assertEqual(self.task.description, 'desc1')
            self.assertIn(self.user1, self.task.user.all())
            self.assertIn(self.user2, self.task.user.all())
            self.assertEqual(self.task.project.name, 'project1')
            
      def test_update_task(self):
            self.task.title = 'Updated-title'
            self.task.save()
            self.assertEqual(self.task.title, 'Updated-title')
            
      def test_delete_task(self):
            task_id = self.task.id
            self.task.delete()
            with self.assertRaises(Task.DoesNotExist):
                Task.objects.get(id=task_id)
      
      def test_task_completed(self):
            self.assertFalse(self.task.completed)
            self.task.completed = True
            self.task.save()
            self.assertTrue(self.task.completed)
            
      def test_filter_tasks_by_user(self):
            another_user = User.objects.create_user(email='anotheruser@mail.com', password='123456')
            new_task = Task.objects.create(
                project=self.project,
                title="new_task_title",
                description="new_desc"
            )
            new_task.user.set([another_user])  
            new_task.save()

            tasks = Task.objects.filter(user=another_user)
            self.assertIn(another_user, new_task.user.all()) 
            self.assertEqual(tasks.count(), 1)  
            self.assertEqual(tasks.first().title, 'new_task_title')  

            
      def test_get_all_tasks(self):
            response = self.client.get('/api/tasks/')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(len(response.json()), 1)
            self.assertEqual(response.json()[0]['title'], 'task')
        
class EmailTestCase(TestCase):
    def test_email(self):
        send_mail(
            'Test',
            'test case',
            settings.EMAIL_HOST_USER,
            ['emirhantavus17@gmail.com'],
            fail_silently=False,
        )            