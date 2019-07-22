import requests

from context_propagation_python import inject
from context_propagation_python.context import get_context

origin_send = None


def register():
    global origin_send
    origin_send = requests.Session.send

    requests.Session.send = send


def send(self, request, **kwargs):
    # type: (requests.Session, requests.Request,dict)-> requests.Response

    if not callable(origin_send):
        raise ValueError("origin_send")

    for k, v in inject.inject(get_context()).items():
        request.headers[k] = v

    return origin_send(self, request, **kwargs)
