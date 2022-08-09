import json
import allure
import conftest
import requests
from data.page import page_base_fields
from helpers.common import random_string

from helpers.media_wiki.login import login_account
from helpers.media_wiki.csrf_token_generate import gen_csrf_token
from helpers.media_wiki.page import get_wiki_page, post_page, search_wiki_pages


class Test_edit_page:

    @allure.title('Test valid edit page')
    def test_valid_edit_page(self):

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
                new_page['text'] = f"New Page Edit Example"
                
                res = post_page(sesh, new_page)

                res_body = res.json()

        with allure.step('Edit an existing page'):

            edit_page = new_page
            edit_page['text'] = f"New Page Edit Example"
            res = post_page(sesh, edit_page)

            res_body = res.json()

            assert res.status_code == 200, f'Expected a 200 status code got {res.status_code}. \nResponse::\n {json.dumps(res_body, indent=4)}'
            page_id = res_body['edit']['pageid']

            res = get_wiki_page(sesh, page_id)
            res_body = res.json()

        with allure.step('Assert the text was updated'):
            assert edit_page['text'] in res_body['parse']['text']['*'], f"Expected a {edit_page['text']} in response. \nResponse::\n {json.dumps(res_body, indent=4)}"
