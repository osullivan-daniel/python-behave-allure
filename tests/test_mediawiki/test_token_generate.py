import json
import allure
import conftest
import requests
from helpers.media_wiki.csrf_token_generate import gen_csrf_token

from helpers.media_wiki.login import login_account

class Test_create_csrf_token:

    @allure.title('Test valid create csrf token')
    def test_valid_create_csrf_token(self):

        with allure.step('Before'):
            sesh = requests.Session()
            username = conftest.crud_user
            password = conftest.crud_password

            with allure.step('Login our test user'):
                res_body = login_account(sesh, username, password)


        with allure.step('Generate a CSRF token'):
            res = gen_csrf_token(sesh)

            assert res.status_code == 200, f'Expected a 200 status code got {res.status_code}. \nResponse::\n {json.dumps(res_body, indent=4)}'
            
            res_body = res.json()
            assert 'csrftoken' in res_body['query']['tokens'], f'Expected to find csrftoken in responce. \nResponse::\n {json.dumps(res_body, indent=4)}'
