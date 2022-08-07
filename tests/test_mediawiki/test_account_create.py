import json
import pytest
import allure
import conftest

from helpers.common import make_get_request, make_post_request
from data.create_user import *

class Test_create_account:

    @allure.title('Test valid create account')
    def test_create_account(self):

        # et some required vars etc
        with allure.step('Before'):
            base_url = conftest.mediawiki_config['base_url']
            full_url = f"{conftest.mediawiki_config['base_url']}{conftest.mediawiki_config['api_end_point']}"
        
        with allure.step('Retrieve account creaton token'):
            status_code, res = make_get_request(full_url, account_creaton_params())
            assert status_code == 200, f'Expected a 200 status code got {status_code}. \nResponse::\n {json.dumps(res, indent=4, sort_keys=True)}'
            print(res)

        with allure.step('Create account'):
            create_user_params = create_test_user_params(res['query']['tokens']['createaccounttoken'], base_url)
            print(create_user_params)
            status_code, res = make_post_request(full_url, create_user_params)
            print(status_code)
            print(res)
            pass

        with allure.step(''):
            pass

        with allure.step(''):
            assert 1==2