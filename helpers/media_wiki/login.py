import json
import conftest

from data.login import *


def login_account(sesh, username: str, password: str, run_assertions: bool = False):

    base_url = f"{conftest.mediawiki_config['base_url']}"
    full_url = f"{conftest.mediawiki_config['base_url']}{conftest.mediawiki_config['api_end_point']}"

    res = sesh.get(url=full_url, params=login_token_params())

    res_body = res.json()

    if run_assertions:
        assert res.status_code == 200, f'Expected a 200 status code got {res.status_code}. \nResponse::\n {json.dumps(res_body, indent=4, sort_keys=True)}'
        assert 'error' and 'warnings' not in res_body, f'Found error/warning in response body. \nResponse::\n {json.dumps(res_body, indent=4, sort_keys=True)}'

    login_token = res_body['query']['tokens']['logintoken']

    login_params = gen_login_parms(username, password, login_token, base_url)

    res = sesh.post(full_url, data=login_params)
    res_body = res.json()

    if run_assertions:
        assert res.status_code == 200, f'Expected a 200 status code got {res.status_code}. \nResponse::\n {json.dumps(res_body, indent=4, sort_keys=True)}'
        assert res_body['clientlogin']['status'] != 'FAIL', f'Status FAIL found. \nResponse::\n {json.dumps(res_body, indent=4, sort_keys=True)}'

    return res_body

