import graphene
from util.storage.s3.util import create_presigned_url_post


class PresignedUrlPostFields(graphene.ObjectType):
    class Meta:
        name = "s3_presigned_url_post_fields"

    key = graphene.String(required=True)
    x_amz_algorithm = graphene.String(required=True)
    x_amz_credential = graphene.String(required=True)
    x_amz_date = graphene.String(required=True)
    policy = graphene.String(required=True)
    x_amz_signature = graphene.String(required=True)

    def resolve_key(parent, info):
        return parent["key"]

    def resolve_x_amz_algorithm(parent, info):
        return parent["x-amz-algorithm"]

    def resolve_x_amz_credential(parent, info):
        return parent["x-amz-credential"]

    def resolve_policy(parent, info):
        return parent["policy"]

    def resolve_x_amz_date(parent, info):
        return parent["x-amz-date"]

    def resolve_x_amz_signature(parent, info):
        return parent["x-amz-signature"]


class PresignedUrlPost(graphene.ObjectType):
    class Meta:
        name = "s3_presigned_url_post"
        description = "Get a presigned URL for file upload to S3"

    url = graphene.String(required=True)
    fields = graphene.Field(PresignedUrlPostFields, required=True)

    def resolve_url(parent, info):
        return parent['url']

    def resolve_fields(parent, info):
        return parent["fields"]


class Query(graphene.ObjectType):
    class Meta:
        name = "s3"

    presigned_url_post = graphene.Field(
        PresignedUrlPost, object_name=graphene.String())

    def resolve_presigned_url_post(parent, info, object_name):
        return create_presigned_url_post(object_name)
