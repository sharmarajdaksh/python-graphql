import requests


class RequestsClient():

    def __init__(self, base_url):
        self.base_url = base_url

    def make_request(self, endpoint=None, method=None, headers=None, data=None, json=None):

        request_func = getattr(requests, method)

        request_endpoint = self.base_url + \
            (endpoint if endpoint is not None else "")

        response = request_func(
            request_endpoint, headers=headers, data=data, json=json)

        return response
