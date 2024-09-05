from django.shortcuts import render
from users.models import User
from users.serializers import UserSerializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny , IsAdminUser
from rest_framework import status
from django.contrib.auth import authenticate , login ,logout
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import Group

class UserView(APIView):
      permission_classes = [IsAdminUser,]
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
      
class UserLoginView(APIView):
      permission_classes =[AllowAny,]
      
      def post(self,request):
            email = request.data.get('email')
            password = request.data.get('password')
            user = authenticate(request,email=email,password=password)
            if user is None:
                  return Response({'message':'user not found '},status=status.HTTP_404_NOT_FOUND)
            login(request,user)
            refresh = RefreshToken.for_user(user)
            return Response({
                  'message':'login is successful',
                  'refresh':str(refresh),
                  'access':str(refresh.access_token),
                  })
            
class UserRoleView(APIView):
      permission_classes = [IsAdminUser,]
      
      def post(self,request):
            user = request.data.get('email')
            developer_group = Group.objects.get(name='Developer')
            user.groups.add(developer_group)
            return Response({'message':'Successful..'},status=status.HTTP_200_OK)