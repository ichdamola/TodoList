from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import PROTECT
from datetime import datetime

class Project(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(default=datetime.now)
    updated = models.DateTimeField(default=datetime.now)

    def __str__(self) -> str:
        return '%s' % self.name

class Task(models.Model):
    project = models.ForeignKey('Project', on_delete=models.CASCADE)
    parent_tasks = models.ForeignKey('Task', null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    text = models.TextField()
    status = models.BooleanField(default=True)
    archived = models.BooleanField(default=False)

    created = models.DateTimeField()
    updated = models.DateTimeField()

    def __str__(self) -> str:
        return '%s' % self.name

