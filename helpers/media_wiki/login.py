import json
import conftest
import requests

from data.login import *
from helpers.common import random_string

def login_account(username: str, password: str, run_assertions: bool = False):
    sesh = requests.Session()

    base_url = conftest.mediawiki_config['base_url']

    res = sesh.get(url=base_url, params=login_token_params())
    res_body = res.json()

    login_token = res_body['query']['tokens']['logintoken']

    if run_assertions:
        assert res.status_code == 200, f'Expected a 200 status code got {res.status_code}. \nResponse::\n {json.dumps(res_body, indent=4, sort_keys=True)}'
        assert 'error' not in res_body, f'Found error in response body. \nResponse::\n {json.dumps(res_body, indent=4, sort_keys=True)}'

    login_params = gen_login_parms(username, password, login_token)

    res = sesh.post(base_url, data=login_params)
    res_body = res.json()

    if run_assertions:
        assert res.status_code == 200, f'Expected a 200 status code got {res.status_code}. \nResponse::\n {json.dumps(res_body, indent=4, sort_keys=True)}'
        # assert res_body['createaccount']['status'] != 'FAIL', f'Status FAIL found. \nResponse::\n {json.dumps(res_body, indent=4, sort_keys=True)}'

    return res_body

