from django.test import TestCase
from projects.models import Project
from rest_framework.test import APIClient , APITestCase
from rest_framework import status
# Create your tests here.

class ProjectModelTest(TestCase):
      def setUp(self):
            self.project = Project.objects.create(
                  name = "project1",
                  description = "description1"
            )
            self.project2 = Project.objects.create(
                  name = "project2",
                  description = "description2"
            )
            self.project3 = Project.objects.create(
                  name = "project3",
                  description = "description3"
            )
            
      def test_exists_project(self):
            self.assertEqual(self.project.name,'project1')
            self.assertEqual(self.project.description,'description1')
            
      def test_project_str_method(self):
            self.assertEqual(str(self.project),'project1')
            
      def test_project_page_exists(self):
            url = self.client.get('/api/projects/')
            self.assertEqual(url.status_code,status.HTTP_200_OK) # Failed until we create /api/projects url.
            
      def test_list_all_projects(self):
           projects = Project.objects.all()
           for project in projects:
                 print(str(project))
           
      def test_projects_count(self):
            projectCount = len(Project.objects.all())
            self.assertEqual(projectCount,3)
            print(projectCount)