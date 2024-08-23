from rest_framework import serializers
from django.contrib.auth import get_user_model
User = get_user_model()

class UserSerializers(serializers.ModelSerializer):
      class Meta:
            model = User
            fields = ('id', 'email', 'password')
            extra_kwargs = {'password': {'write_only': True}}
            
      def create(self, validated_data):
            user = User.objects.create_user(
                  email=validated_data['email']
            )
            user.set_password(validated_data['password']) #hs256
            user.save()
            return user