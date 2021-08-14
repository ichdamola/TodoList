import graphene
from graphene.pyutils.version import get_version
from graphene.types import schema

import tasks.schema

class Query(tasks.schema.Query, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)
