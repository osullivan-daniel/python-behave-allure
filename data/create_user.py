def account_creation_params():
    return {
            "action":"query",
            "meta":"tokens",
            "type":"createaccount",
            "format":"json"
        }


def create_test_user_params(token: str, username:str, password:str, url:str):
    return {
            "action": "createaccount",
            "createtoken": token,
            "username": username,
            "password": password,
            "retype": password,
            "createreturnurl": url,
            "format": "json"
        }
