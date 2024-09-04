from rest_framework import serializers
from tasks.models import Task

class TaskSerializers(serializers.ModelSerializer):
      project_name = serializers.CharField(source="project.name",read_only=True)
      user_emails = serializers.SerializerMethodField()
      
      class Meta:
            model = Task
            fields = ('id','title','description','project_name','completed','deadline','user_emails')
      
      def get_user_emails(self, obj):
            return [user.email for user in obj.user.all()]