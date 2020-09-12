import graphene

from config.github import GITHUB_CLIENT_ID, GITHUB_OAUTH_LOGIN_REDIRECT_URL


class Query(graphene.ObjectType):
    class Meta:
        name = "github"

    github_login_url = graphene.String()

    def resolve_github_login_url(parent, info):
        return f"{GITHUB_OAUTH_LOGIN_REDIRECT_URL}?client_id={GITHUB_CLIENT_ID}&scope=user"
