from django.test import TestCase
from .models import User
from django.shortcuts import get_object_or_404

class UserModelTest(TestCase):
      def setUp(self):
            self.user = User.objects.create_user(
                  email = 'test@mail.com',
                  password = '123456',
                  first_name = 'firstname',
                  last_name = 'lastname'
            )
            
      def test_user_creation(self):
            self.assertEqual(self.user.email,'test@mail.com')
            self.assertTrue(self.user.check_password('123456'))
            self.assertEqual(self.user.first_name,'firstname')
            self.assertEqual(self.user.last_name,'lastname')
            
      def test_superuser_creation(self):
            superuser = User.objects.create_superuser(
                  email = 'admin@mail.com',
                  password = '123456',
                  first_name = 'fname',
                  last_name = 'lname'
            )
            self.assertEqual(superuser.email,'admin@mail.com')
            self.assertTrue(superuser.check_password('123456'))
            

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase , APIClient

class UserTokenAuthTest(APITestCase):
      def setUp(self):
            self.user = User.objects.create_user(
                  email = 'authtest@mail.com',
                  password = '123456'
            )
            
      def test_obtain_token(self):
            #get token after login
            url = reverse('token_obtain_pair') # api/token/
            data = {
                  'email':'authtest@mail.com',
                  'password':'123456'
            }
            resp = self.client.post(url,data)
            self.assertEqual(resp.status_code, status.HTTP_200_OK)
            self.assertIn('access', resp.data)  # error with 401 status code when email is wrong;
            self.assertIn('refresh', resp.data)  # but when it's right, status code is 200 ok
            
      def test_invalid_login(self):
            url = reverse('token_obtain_pair') # with wrong email and pass, can't login and get token
            data = {
                  'email':'authtestwrong@mail.com',
                  'password':'wrongpass'
            }
            resp = self.client.post(url,data)
            self.assertEqual(resp.status_code,status.HTTP_401_UNAUTHORIZED)
            

class GetUserListTest(TestCase):
      def setUp(self):
            self.client = APIClient()
            
            self.user1 = User.objects.create_user(
            email='user1@mail.com',
            password='123456',
            first_name='User',
            last_name='One'
        )
            self.user2 = User.objects.create_user(
            email='user2@mail.com',
            password='123456',
            first_name='User',
            last_name='Two'
        )
            
            
      def test_users_page_exists(self):
            url = reverse('user-list') #'/api/users'
            resp = self.client.get(url)
            self.assertEqual(resp.status_code,status.HTTP_200_OK)
            
      def test_single_user(self):
            users = User.objects.get(email='user1@mail.com')