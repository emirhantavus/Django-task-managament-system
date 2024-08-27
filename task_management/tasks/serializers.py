from rest_framework import serializers
from tasks.models import Task

class TaskSerializers(serializers.ModelSerializer):
      project_name = serializers.CharField(source="project.name",read_only=True)
      user_email = serializers.CharField(source="user.email",read_only=True)
      class Meta:
            model = Task
            fields = ('id','title','description','project_name','user_email')