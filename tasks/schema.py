from graphene import ObjectType, InputObjectType, List, Mutation, String, Boolean, Int, ID
from graphene.types.field import Field
from graphene_django import DjangoObjectType
from graphql import GraphQLError
from django.db.models import Q
from .models import Project, Task

class ProjectType(DjangoObjectType):
    class Meta:
        model = Project  

class TaskType(DjangoObjectType):
    class Meta:
        model = Task   

class CreateProject(Mutation):
    class Arguments:
        name = String()

    ok = Boolean()
    project = Field(lambda: ProjectType)

    def mutate(self, info, name):
        user = info.context.user
        project = Project.objects.create(name=name, user=user)
        ok = True
        return CreateProject(project=project, ok=ok)

class CreateTask(Mutation):
    class Arguments:
        name = String(required=True)
        text = String(required=True)
        projectid = Int(required=True)

    ok = Boolean()
    task = Field(lambda: TaskType)

    def mutate(self, info, name, text, projectid):
        task = Task.objects.create(name=name, text=text, project_id=projectid)

        ok = True
        return CreateTask(task=task, ok=ok)

class DeleteProject(Mutation):
    class Arguments:
        id = ID()

    ok = Boolean()
    project = Field(lambda: ProjectType)

    def mutate(self, info, id):
        project = Project.objects.get(id=id)
        project.delete()
        ok=True
        return DeleteProject(project=project, ok=ok)

class DeleteTask(Mutation):
    class Arguments:
        id = ID()

    ok = Boolean()
    task = Field(lambda: TaskType)

    def mutate(self, info, id):
        user = info.context.user
        task = Task.objects.get(id=id)

        # if user.is_anonymous:
        #     raise GraphQLError("user must logged in to update a task.")

        task.delete()
        ok=True
        return DeleteTask(task=task, ok=ok)


# class Query(ObjectType):
#     projects = List(ProjectType)
#     tasks = List(TaskType)

#     def resolve_projects(self, info, **kwargs):
#         return Project.objects.all()
    
#     def resolve_tasks(self, info, **kwargs):
#         return Task.objects.select_related().all()

class Query(ObjectType):
    tasks = List(TaskType, search=String())

    def resolve_tasks(self, info, search=None):
        print(search)
        if search:
            filtered = (
                Q(name__contains=search) |
                Q(text__contains=search) 
            )
            return Task.objects.filter(filtered)

        return Task.objects.all()
    
