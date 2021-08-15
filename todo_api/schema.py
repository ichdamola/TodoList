import graphene
from graphene.pyutils.version import get_version
from graphene.types import schema

import tasks.schema

class Query(tasks.schema.Query, graphene.ObjectType):
    pass

class MyMutation(graphene.ObjectType):
    create_project = tasks.schema.CreateProject.Field()
    create_task = tasks.schema.CreateTask.Field()
    delete_task = tasks.schema.DeleteTask.Field()
    delete_project = tasks.schema.DeleteProject.Field()

schema = graphene.Schema(query=Query, mutation=MyMutation)
