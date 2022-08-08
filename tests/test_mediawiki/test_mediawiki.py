import json
import allure
import requests

from data.page import page_base_fields

from helpers.common import random_string
from helpers.media_wiki.login import login_account
from helpers.media_wiki.page import get_wiki_page, post_page, search_wiki_pages
from helpers.media_wiki.create_account import create_new_account
from helpers.media_wiki.csrf_token_generate import gen_csrf_token

class Test_mediawiki:

    @allure.title('Test mediawiki')
    def test_mediawiki(self):

        with allure.step('Before'):
            sesh = requests.Session()

        with allure.step('Create new account'):
            username, password, res_body = create_new_account(sesh, run_assertions=True)
       
        # alternate if no endpoint
        with allure.step('Loggin new account to verify it was created'):
            res_body = login_account(sesh, username, password, run_assertions=True)
            
            assert 'PASS' in res_body['clientlogin']['status'], \
            f'''We shouldnt get the status PASS when we successfully log in
            please check the message for more details.\nResponse::\n {json.dumps(res_body, indent=4)}'''

        with allure.step('Generate a CSRF token'):
            res = gen_csrf_token(sesh)

            assert res.status_code == 200, f'Expected a 200 status code got {res.status_code}. \nResponse::\n {json.dumps(res_body, indent=4)}'
            
            res_body = res.json()
            assert 'csrftoken' in res_body['query']['tokens'], f'Expected to find csrftoken in responce. \nResponse::\n {json.dumps(res_body, indent=4)}'


        with allure.step('Create new page'):
            csrf_token = res_body['query']['tokens']['csrftoken']
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
