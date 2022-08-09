def login_token_params():
    return {
            "action":"query",
            "meta":"tokens",
            "type":"login",
            "format":"json"
        }


def gen_login_parms(user: str, password: str, lgtoken: str, url: str):
    return {
            "action":"clientlogin",
            "username": user,
            "password": password,
            "logintoken": lgtoken,
            "loginreturnurl": url,
            "format":"json"
        }
