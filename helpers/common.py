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


def make_request(method: str, url: str) -> Response:
    headers = {'Cache-Control': 'no-cache'}

    res = requests.request(method = method,
                        url = url,
                        headers = headers)     

    return res.status_code, json.loads(res.content)   
