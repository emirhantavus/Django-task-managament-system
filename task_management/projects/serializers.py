from rest_framework import serializers
from projects.models import Project

class projectSerializer(serializers.ModelSerializer):
      class Meta:
            model = Project
            fields = ('id','name','description')