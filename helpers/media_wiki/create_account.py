import json
import conftest

from data.create_user import *
from helpers.common import random_string

def create_new_account(sesh, username: str = None, password: str = None, run_assertions: bool = False):
    
    base_url = conftest.mediawiki_config['base_url']
    full_url = f"{conftest.mediawiki_config['base_url']}{conftest.mediawiki_config['api_end_point']}"

    res = sesh.get(url=full_url, params=account_creation_params())
    res_body = res.json()

    if run_assertions:
        assert res.status_code == 200, f'Expected a 200 status code got {res.status_code}. \nResponse::\n {json.dumps(res_body, indent=4, sort_keys=True)}'
        assert 'error' or 'warnings' not in res_body, f'Found error/warning in response body. \nResponse::\n {json.dumps(res_body, indent=4, sort_keys=True)}'

    create_account_token = res_body['query']['tokens']['createaccounttoken']

    username = random_string() if username is None else username
    password = random_string(10) if password is None else password

    test_user_params = create_test_user_params(create_account_token, username, password, base_url)

    res = sesh.post(full_url, data=test_user_params)
    res_body = res.json()

    if run_assertions:
        assert res.status_code == 200, f'Expected a 200 status code got {res.status_code}. \nResponse::\n {json.dumps(res_body, indent=4, sort_keys=True)}'
        assert res_body['createaccount']['status'] != 'FAIL', f'Status FAIL found. \nResponse::\n {json.dumps(res_body, indent=4, sort_keys=True)}'

    return username, password, res_body

