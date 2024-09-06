from django.shortcuts import render
from tasks.models import Task
from tasks.serializers import TaskSerializers
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework import status
from tasks.repositories.task_repository import TaskRepository
from tasks.services.task_service import TaskService
from .tasks import send_task_notification
from users.permissions import IsProjectManager, IsDeveloper
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from django.contrib.auth import get_user_model
from projects.models import Project

User = get_user_model()

class TaskViewSet(ModelViewSet):
      queryset = Task.objects.all()
      serializer_class = TaskSerializers
      
      
class TaskListCreateAPIView(APIView):
      def get(self,request):
            user = request.user
            tasks = TaskRepository.get_tasks_by_user(user)
            serializer = TaskSerializers(tasks, many=True)
            return Response(serializer.data)

      def post(self, request):
            if request.user.groups.filter(name='Developer').exists():
                return Response({'error': 'Developer can not create tasks'}, status=status.HTTP_403_FORBIDDEN)

            if request.user.groups.filter(name='Project Manager').exists():
                user_email = request.data.get('user')
                project_id = request.data.get('project')
                title = request.data.get('title')
                description = request.data.get('description')          
                try:
                    user = User.objects.get(email=user_email)
                    project = Project.objects.get(id=project_id)
                    task = Task(project=project, title=title, description=description)
                    task.save()
                    task.user.add(user)
                    serializer = TaskSerializers(task)
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                except User.DoesNotExist:
                    return Response({'error': 'User does not exist'}, status=status.HTTP_400_BAD_REQUEST)
                except Project.DoesNotExist:
                    return Response({'error': 'Project does not exist'}, status=status.HTTP_400_BAD_REQUEST)
                except Exception as e:
                    return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'error': 'You do not have permission to create tasks'}, status=status.HTTP_403_FORBIDDEN)
            
            
class TaskCompleteView(APIView):
    def patch(self, request, pk):
        try:
            task = Task.objects.get(pk=pk)
            task.completed = True
            task.save()
            send_task_notification.delay(task.id)
            serializer = TaskSerializers(task)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Task.DoesNotExist:
            return Response({'error': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)