import graphene

from auth.github.mutation import GithubAuthorize


class Mutation(graphene.ObjectType):
    authorize_with_github = GithubAuthorize.Field()
