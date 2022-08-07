def account_creaton_params():
    return{
            "action":"query",
            "meta":"tokens",
            "type":"createaccount",
            "format":"json"
        }

def create_test_user_params(token: str, url:str):
    return{
            "action": "createaccount",
            "createtoken": token,
            "username": "test_user",
            "password": "vmaJenMU",
            "retype": "vmaJenMU",
            "createreturnurl": url,
            "format": "json"
        }
