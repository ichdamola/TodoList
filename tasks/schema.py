from graphene import ObjectType, List
from graphene_django import DjangoObjectType
from .models import Project, Task

class ProjectType(DjangoObjectType):
    class Meta:
        model = Project    

class TaskType(DjangoObjectType):
    class Meta:
        model = Task   

class Query(ObjectType):
    projects = List(ProjectType)
    tasks = List(TaskType)

    def resolve_projects(self, info, **kwargs):
        return Project.objects.all()
    
    def resolve_tasks(self, info, **kwargs):
        return Task.objects.select_related().all()
    
