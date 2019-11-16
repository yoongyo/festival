from festival.schema import Query as FestivalQuery
from accounts.schema import Query as UserQuery
import graphene


class Query(FestivalQuery, UserQuery, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
