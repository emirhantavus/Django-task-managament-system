from django.shortcuts import render
from projects.models import Project
from projects.serializers import projectSerializer
from rest_framework.viewsets import ModelViewSet

class ProjectViewSet(ModelViewSet):
      queryset = Project.objects.all()
      serializer_class = projectSerializer