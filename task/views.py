from django.shortcuts import render
from rest_framework import status, viewsets, generics
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from task.models import Task
from django_filters.rest_framework import DjangoFilterBackend

# Serializers
from task.serializers import taskModelSerializer

class userCreatetaskView(APIView):
    permission_classes = ''
    
    def post(self,request):
        serializer = taskModelSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
class listtaskView(APIView):
    permission_classes = ''
    
    def get(self,request):
        tasks = Task.objects.all()
        tasks_data = taskModelSerializer(tasks, many = True).data
        return Response(tasks_data)
    
class updatetaskView(APIView):
    permission_classes = ''
    
    def put(self,request):
        task = Task.objects.filter(id = 1).first()
        task_serializer = taskModelSerializer(task,data = request.data)
        if task_serializer.is_valid():
            task_serializer.save()
            return Response(task_serializer.data)
        return Response(task_serializer.errors)
    
class deletetaskView(APIView):
    permission_classes = ''
    
    def delete(self,request):
        
        task = Task.objects.filter(id = 5).first()
        task.delete()
        return Response('ELIMINADO')
    
class filterstatusView(generics.ListAPIView):
    
    queryset = Task.objects.all()
    serializer_class = taskModelSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status']
    
class filterusertask(generics.ListAPIView):
    permission_classes = [IsAdminUser]
    queryset = Task.objects.all()
    serializer_class = taskModelSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['assigned_to']
    
    
    
    
    
    

        
        
    

        
        
        
        
    
