from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100, blank=True, null=True,default=None)
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE,related_name='tasks')
    status = models.CharField(max_length=20, choices=(
        ('to_do', 'To do'),
        ('done', 'Done'),
    ), default='to_do')
    coment = models.CharField(max_length=100, blank=True, null=True, default=None)