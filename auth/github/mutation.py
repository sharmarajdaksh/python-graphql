import graphene

from auth.github.utils import get_github_oauth_response
from auth.github.types import GithubUserdata


class GithubAuthorize(graphene.Mutation):
    class Arguments:
        code = graphene.String(name="code")

    user_data = graphene.Field(GithubUserdata)

    def mutate(root, info, code):
        github_user_data = get_github_oauth_response(code)
        user_data = GithubUserdata(
            name=user_data["name"], email=user_data["email"], avatar_url=user_data["avatar_url"])

        return GithubAuthorize(user_data=user_data)
