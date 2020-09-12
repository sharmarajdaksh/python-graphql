import graphene
from util.storage.s3.query import Query as S3Query


class Query(graphene.ObjectType):
    class Meta:
        name = "storage"

    s3 = graphene.Field(S3Query, name="s3")

    def resolve_s3(parent, info):
        return S3Query()
