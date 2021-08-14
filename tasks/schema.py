import graphene
from .models import Project, Task
from graphene_django import DjangoObjectType

class Projects(DjangoObjectType):
    class Meta:
        model = Project    

class Query(graphene.ObjectType):
    projects = graphene.List(Projects)

    def resolve_projects(self, info):
        return Project.objects.all()

schema = graphene.Schema(query=Query)