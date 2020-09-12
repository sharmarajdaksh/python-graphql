import graphene
from util.query import Query as UtilQuery
from auth.query import Query as AuthQuery


class Query(graphene.ObjectType):
    name = "query"

    auth = graphene.Field(AuthQuery, name="auth")
    util = graphene.Field(UtilQuery, name="util")

    def resolve_util(root, info):
        return UtilQuery()

    def resolve_auth(root, info):
        return AuthQuery()
