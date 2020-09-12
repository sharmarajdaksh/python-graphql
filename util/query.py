import graphene
from util.storage.query import Query as StorageQuery


class Query(graphene.ObjectType):
    class Meta:
        name = "util"

    storage = graphene.Field(StorageQuery, name="storage")

    def resolve_storage(parent, info):
        return StorageQuery()