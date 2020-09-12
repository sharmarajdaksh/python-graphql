import graphene

from auth.github.query import Query as GithubQuery


class Query(graphene.ObjectType):
    class Meta:
        name = "auth"

    github = graphene.Field(GithubQuery, name="github")

    def resolve_github(parent, info):
        return GithubQuery()
