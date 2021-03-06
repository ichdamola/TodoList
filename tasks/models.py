from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import PROTECT
from datetime import datetime

class Project(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return '%s' % self.name

class Task(models.Model):
    project = models.ForeignKey('Project', on_delete=models.CASCADE, related_name='tasks')
    parent_tasks = models.ForeignKey('Task', null=True, blank=True, on_delete=models.CASCADE, related_name='child_tasks')
    name = models.CharField(max_length=100)
    text = models.TextField()
    status = models.BooleanField(default=True)
    archived = models.BooleanField(default=False)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return '%s' % self.name

