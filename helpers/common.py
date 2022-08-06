from email import header
import os
import json
import requests

from requests.models import Response


def load_configs(name: str) -> str:
    filepath = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'configs/env.json'))
    with open(filepath) as input:
        data = json.load(input)
        return data[name]


def make_request(method: str, url: str) -> Response:

    headers = {}

    res = requests.request(method = method,
                           url = url,
                           headers = headers)           