
from rest_framework import serializers
from task.models import Task

class taskModelSerializer(serializers.ModelSerializer):
    
    class Meta:

        model = Task
        fields = (
            'name',
            'description',
            'assigned_to',
            'status',
            'coment',
        )