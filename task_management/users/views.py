from django.shortcuts import render
from users.models import User
from users.serializers import UserSerializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status

class UserView(APIView):
      def get(self,request):
            users = User.objects.all()
            serializer = UserSerializers(users, many=True)
            return Response(serializer.data)
      
class UserRegisterView(APIView):
      permission_classes =[AllowAny,]
      def post(self, request):
       serializer = UserSerializers(data=request.data)
       if serializer.is_valid():
           user = serializer.save()
           tokens = user.tokens()
           return Response(tokens, status.HTTP_201_CREATED)
       return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)