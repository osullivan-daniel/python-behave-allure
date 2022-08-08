import json
import allure
import conftest
import requests
from data.page import page_base_fields
from helpers.common import random_string

from helpers.media_wiki.login import login_account
from helpers.media_wiki.csrf_token_generate import gen_csrf_token
from helpers.media_wiki.page import post_page, search_wiki_pages


class Test_create_page:

    @allure.title('Test valid create page')
    def test_valid_create_page(self):

        with allure.step('Before'):
            sesh = requests.Session()
            username = conftest.crud_user
            password = conftest.crud_password

            with allure.step('Login our test user'):
                res_body = login_account(sesh, username, password)

            with allure.step('Generate a CSRF token'):
                res = gen_csrf_token(sesh)
                res_body = res.json()
                csrf_token = res_body['query']['tokens']['csrftoken']

        with allure.step('Create new page'):
            test_page_title = f"Test Page {random_string()}"

            new_page = page_base_fields(csrf_token)
            new_page['title'] = test_page_title
            new_page['text'] = f"New Page Create Example"
            
            res = post_page(sesh, new_page)

            res_body = res.json()
            assert res.status_code == 200, f'Expected a 200 status code got {res.status_code}. \nResponse::\n {json.dumps(res_body, indent=4)}'
            assert res_body['edit']['result'] == 'Success', f'Expected to find Success in response. \nResponse::\n {json.dumps(res_body, indent=4)}'


        with allure.step('Ensure new page appears in all page list'):
            res = search_wiki_pages(sesh, test_page_title)
            res_body = res.json()
            assert res.status_code == 200, f'Expected a 200 status code got {res.status_code}. \nResponse::\n {json.dumps(res_body, indent=4)}'

            found = False
            for each in res_body['query']['allpages']:
                if each['title'] == test_page_title:
                    found = True
                break
            
            assert found == True, f'Expected to find {test_page_title} in response. \nResponse::\n {json.dumps(res_body, indent=4)}'


    @allure.title('Test create page without valid CSRF token')
    def test_invalid_create_page(self):

        with allure.step('Before'):
            sesh = requests.Session()
            username = conftest.crud_user
            password = conftest.crud_password
            invalid_csrf_token = random_string(20)

            with allure.step('Login our test user'):
                res_body = login_account(sesh, username, password)

        with allure.step('Create new page'):
            test_page_title = f"Test Page {random_string()}"

            new_page = page_base_fields(invalid_csrf_token)
            new_page['title'] = test_page_title
            new_page['text'] = f"New Page Create Example"
            
            res = post_page(sesh, new_page)

            res_body = res.json()
        
        with allure.step('Assert new page was not created'):
            assert res_body['error']['code'] == 'badtoken', f'Expected to find badtoken in response. \nResponse::\n {json.dumps(res_body, indent=4)}'
