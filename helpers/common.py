from email import header
import os
import json
import requests

from requests.models import Response

def load_configs(name: str) -> str:
    filepath = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', f'configs/{name}.json'))
    with open(filepath) as input:
        data = json.load(input)
        return data[name]

def make_get_request(url: str, params: json = None) -> Response:
    return __make_request__('GET', url, params=params)

def make_post_request(url: str, data:json = None) -> Response:
    return __make_request__('POST', url, data=data)

def __make_request__(method: str, url: str, params: json = None, data: json = None) -> Response:
    headers = {'Cache-Control': 'no-cache'}

    res = requests.request(method = method,
                           url = url,
                           headers = headers,
                           params=params,
                           data=data)

    return res.status_code, json.loads(res.content)   

