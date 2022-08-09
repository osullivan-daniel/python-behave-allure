import pytest
import requests

from helpers.common import load_configs
from helpers.media_wiki.create_account import create_new_account

mediawiki_config = None
crud_user = None
crud_password = None

def pytest_configure():
    global mediawiki_config
    mediawiki_config = load_configs('mediawiki')


@pytest.fixture(scope="session", autouse=True)
def create_user_for_crud_tests():
    global crud_user, crud_password
    sesh = requests.Session()
    
    # To make the tests portable we create a user before all tests, 
    # an alternative would be to seed the db with one for all test runs  
    crud_user, crud_password, res_body = create_new_account(sesh)
