import graphene


class GithubUserdata(graphene.ObjectType):
    class Meta:
        name = "github_user_data"

    name = graphene.String()
    email = graphene.String()
    avatar_url = graphene.String()
