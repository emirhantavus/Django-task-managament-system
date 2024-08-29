from django.test import TestCase
from django.contrib.auth import get_user_model
from tasks.models import Task
from projects.models import Project

User = get_user_model()

class TaskTestCase(TestCase):
      def setUp(self):
            self.user = User.objects.create_user(email='user1@mail.com', password='123456')
            self.project = Project.objects.create(name='project1', description='desc1')
            self.task = Task.objects.create(
                        project = self.project,
                        user = self.user,
                        title = 'task',
                        description = 'desc1',
                        completed = False
                  )
            

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
      
      def test_task_str_method(self):
            self.assertEqual(str(self.task),"task")
            
      def test_task_exists(self):
            self.assertEqual(self.task.title,'task')
            self.assertEqual(self.task.description,'desc1')
            self.assertEqual(self.task.user.email,'user1@mail.com')
            self.assertEqual(self.task.project.name,'project1')
            
      def test_update_task(self):
            self.task.title = 'Updated-title'
            self.task.save()
            self.assertEqual(self.task.title,'Updated-title')
            
      def test_delete_task(self):
            task_id = self.task.id
            #print(Task.objects.get(id=task_id))
            self.task.delete()
            with self.assertRaises(Task.DoesNotExist):
                  print(Task.objects.get(id=task_id))
      
      def test_task_completed(self):
            self.assertFalse(self.task.completed)
            self.task.completed = True
            self.task.save()
            self.assertTrue(self.task.completed)
            
      def test_filter_tasks_by_user(self):
            another_user = User.objects.create_user(email='anotheruser@mail.com',password='123456')
            Task.objects.create(
                  project = self.project,
                  user = another_user,
                  title = "new_task_title",
                  description = "new_desc"
            )
            tasks = Task.objects.filter(user=another_user)
            self.assertEqual(tasks[0].user.email,'anotheruser@mail.com')
            self.assertEqual(tasks.count(),1)
            self.assertEqual(tasks[0].title,'new_task_title')
            
      def test_get_all_tasks(self):
            response = self.client.get('/api/tasks/')
            self.assertEqual(response.status_code,200)
            self.assertEqual(len(response.data),1)
            self.assertEqual(response.data[0]['title'],'task')