# Django REST Framework
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser


# Serializers
from users.serializers import UserLoginSerializer, UserModelSerializer

# Models
from users.models import User
    
class UserloginView(APIView):
    permission_classes = ''
    
    def post(self, request):
        
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, token = serializer.save()
        data = {
            'user': UserModelSerializer(user).data,
            'access_token': token
        }
        return Response(data, status=status.HTTP_201_CREATED)
    
class UsercreateView(APIView):
    permission_classes = ''
    
    def post(self,request):
        serializer = UserModelSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        user.set_password(request.data['password'])
        user.save()
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
class UserlistView(APIView):
    permission_classes = ''
    
    def get(self,request):
        users = User.objects.all()
        user_data = UserModelSerializer(users, many = True).data
        return Response(user_data)
    

class userfilterView(APIView):
    permission_classes = ''
    
    def get(self,request):
        
        user = User.objects.filter(id = 1).first()
        user_serializer = UserModelSerializer(user)
        return Response(user_serializer.data)

class deletetaskView(APIView):
    permission_classes = ''
    
    def delete(self,request):
        
        user = User.objects.filter(id = 1).first()
        user.delete()
        return Response('ELIMINADO')    