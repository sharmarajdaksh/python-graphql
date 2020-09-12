def get_requests_client(base_url):
    from util.api.client import RequestsClient
    return RequestsClient(base_url)
