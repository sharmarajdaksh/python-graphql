from config.github import GITHUB_CLIENT_ID, GITHUB_CLIENT_SECRET, GITHUB_OAUTH_TOKEN_URL, GITHUB_OAUTH_USERDATA_URL
from util.api import get_requests_client


def get_github_access_token(code):
    requests_client = get_requests_client(GITHUB_OAUTH_TOKEN_URL)

    request_headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
    }

    request_json = {
        "client_id": GITHUB_CLIENT_ID,
        "client_secret": GITHUB_CLIENT_SECRET,
        "code": code,
    }

    response = requests_client.make_request(
        method="post", headers=request_headers, json=request_json)

    return response.json()


def get_github_user_data(access_token):
    requests_client = get_requests_client(GITHUB_OAUTH_USERDATA_URL)

    response = requests_client.make_request(
        endpoint=f"?access_token={access_token}", method="get")

    return response.json()


def get_github_oauth_response(code):

    access_token_response = get_github_access_token(code)
    access_token = access_token_response["access_token"]

    user_data = get_github_user_data(access_token)

    return user_data
