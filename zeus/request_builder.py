"""Class specific for handling requests"""

from zeus import config
import requests

cnf = config.get_instance()

AUTH=("null", cnf.get_default_setting("PAT"))
API=cnf.get_default_setting("URL") + "/" + cnf.get_default_setting("PROJECT") + "/_apis"

def build_request(method, resource, **kwargs):

    resource = API + "/" + resource

    #add authentication to every request
    kwargs["auth"] = AUTH
    return requests.request(method, resource, **kwargs)

def get(resource, **kwargs):
    return build_request("GET", resource, **kwargs)

def post(resource, **kwargs):
    return build_request("POST", resource, **kwargs)

def request_ok(request_obj):

    try:
       return request_obj.ok
    except Exception:
        return False

    

