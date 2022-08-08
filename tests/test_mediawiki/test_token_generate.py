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
            res_body = gen_csrf_token(sesh)

            print(res_body)
            assert 1==2

            
        # with allure.step('Create new account'):
            
       
        # # alternate if no endpoint
        # with allure.step('Loggin new account to verify it was created'):
            
            
