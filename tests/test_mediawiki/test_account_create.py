import json
import allure

from helpers.media_wiki.login import login_account
from helpers.media_wiki.create_account import create_new_account


class Test_create_account:

    @allure.title('Test valid create account')
    def test_create_account(self):

        with allure.step('Create new account'):
            username, password, res_body = create_new_account(run_assertions=True)
       
        # alternate if no endpoint
        with allure.step('Loggin new account to verify it was created'):
            res_body = login_account(username, password)
            print(res_body)
            assert 1==2


    # @allure.title('Test unable to create second account with the same username')
    # def test_create_duplicate_account(self):

    #     with allure.step('Create new account'):
    #         username, password, res_body = create_new_account()
                    
    #     with allure.step('Attempt to create account with samename'):
    #         username, password, res_body = create_new_account(username=username)
                        
    #         # There is no message code in valid messages so it should be there
    #         assert 'messagecode' in res_body['createaccount'], \
    #         f'''We shouldnt be able to create two accounts with the same user name 
    #         please check the message for more details. \nResponse::\n {json.dumps(res_body, indent=4, sort_keys=True)}'''

    #         # if the message code is there we expect it to be userexists
    #         assert res_body['createaccount']['messagecode'] == 'userexists', \
    #         f'''We shouldnt be able to create two accounts with the same user name 
    #         please check the message for more details. \nResponse::\n {json.dumps(res_body, indent=4, sort_keys=True)}'''
