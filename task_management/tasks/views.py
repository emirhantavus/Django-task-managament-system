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
            user_email = request.data.get('user')
            project = request.data.get('project')
            title = request.data.get('title')
            description = request.data.get('description')
            try:
                  task = TaskService.create_task(user_email,project,title,description)
                  serializer = TaskSerializers(task)
                  return Response(serializer.data,status=status.HTTP_201_CREATED)
            except ValueError as e:
                  return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
            
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