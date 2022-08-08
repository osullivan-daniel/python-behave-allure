import json
import allure
import requests

from helpers.media_wiki.login import login_account
from helpers.media_wiki.create_account import create_new_account


class Test_create_account:

    @allure.title('Test valid create account')
    def test_create_account(self):

        with allure.step('Before'):
            sesh = requests.Session()

        with allure.step('Create new account'):
            username, password, res_body = create_new_account(sesh, run_assertions=True)
       
        # alternate if no endpoint
        with allure.step('Loggin new account to verify it was created'):
            res_body = login_account(sesh, username, password, run_assertions=True)
            
            assert 'PASS' in res_body['clientlogin']['status'], \
            f'''We shouldnt get the status PASS when we successfully log in
            please check the message for more details.\nResponse::\n {json.dumps(res_body, indent=4, sort_keys=True)}'''


    @allure.title('Test unable to create second account with the same username')
    def test_create_duplicate_account(self):
        
        with allure.step('Before'):
            sesh = requests.Session()

        with allure.step('Create new account'):
            username, password, res_body = create_new_account(sesh)
                    
        with allure.step('Attempt to create account with samename'):
            username, password, res_body = create_new_account(sesh, username=username)
                        
            # There is no message code in valid messages so it should be there
            assert 'messagecode' in res_body['createaccount'], \
            f'''We shouldnt be able to create two accounts with the same user name 
            please check the message for more details. \nResponse::\n {json.dumps(res_body, indent=4, sort_keys=True)}'''

            # if the message code is there we expect it to be userexists
            assert res_body['createaccount']['messagecode'] == 'userexists', \
            f'''We shouldnt be able to create two accounts with the same user name 
            please check the message for more details. \nResponse::\n {json.dumps(res_body, indent=4, sort_keys=True)}'''
