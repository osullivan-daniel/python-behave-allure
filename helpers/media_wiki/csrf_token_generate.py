import json
import conftest

from data.create_user import *
from data.csrf_token import csrf_token_params

def gen_csrf_token(sesh):
    full_url = f"{conftest.mediawiki_config['base_url']}{conftest.mediawiki_config['api_end_point']}"

    res = sesh.get(url=full_url, params=csrf_token_params())
    return res.json()
