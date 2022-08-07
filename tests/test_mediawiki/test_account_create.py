import json
import allure
from helpers.media_wiki.create_account import create_new_account

class Test_create_account:

    @allure.title('Test valid create account')
    def test_create_account(self):

        with allure.step('Create new account'):
            res_body, password = create_new_account()

        # look for an endpoint to do this
        with allure.step('Get account info to verify it was created'):
            pass
        
        # alternate if no endpoint
        with allure.step('Loggin new account to verify it was created'):
            pass




    @allure.title('Test unable to create second account with the same username')
    def test_create_duplicate_account(self):

        with allure.step('Create new account'):
            res_body, password = create_new_account()
            username = res_body['createaccount']['username']

        
        with allure.step('Attempt to create account with samename'):
            res_body, password = create_new_account(username=username, run_assertions=False)
                        
            # There is no message code in valid messages so it should be there
            assert 'messagecode' in res_body['createaccount'], \
            f'''We shouldnt be able to create two accounts with the same user name 
            please check the message for more details. \nResponse::\n {json.dumps(res_body, indent=4, sort_keys=True)}'''

            # if the message code is there we expect it to be userexists
            assert res_body['createaccount']['messagecode'] == 'userexists', \
            f'''We shouldnt be able to create two accounts with the same user name 
            please check the message for more details. \nResponse::\n {json.dumps(res_body, indent=4, sort_keys=True)}'''
