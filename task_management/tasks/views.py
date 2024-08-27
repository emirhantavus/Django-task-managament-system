from django.shortcuts import render
from tasks.models import Task
from tasks.serializers import TaskSerializers
from rest_framework.viewsets import ModelViewSet

class TaskViewSet(ModelViewSet):
      queryset = Task.objects.all()
      serializer_class = TaskSerializers