"""Class specific for handling requests"""

import requests

def build_request(method, url, **kwargs):
    return requests.request(method, url, **kwargs)

def get(url, **kwargs):
    return build_request("GET", url, **kwargs)

def post(url, **kwargs):
    return build_request("POST", url, **kwargs)

def request_ok(request_obj):

    try:
       return request_obj.ok
    except Exception:
        return False
    

