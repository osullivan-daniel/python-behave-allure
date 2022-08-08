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

        with allure.step('Generate page data'):
            new_page = page_base_fields(csrf_token)
            test_page = f"Test_{random_string()}"
            new_page['title'] = test_page
            new_page['text'] = f"New Page Create Example"
            
            res = post_page(sesh, new_page)

            res = search_wiki_pages(sesh, 'New')

            print(res.status_code)
            print(res.content)
            print(res.json())
            assert 1==2



