def login_token_params():
    return {
        'action':"query",
        'meta':"tokens",
        'type':"login",
        'format':"json"
    }

def gen_login_parms(user: str, password: str, lgtoken:str):
    return {
        'action':"login",
        'lgname': user,
        'lgpassword':password,
        'lgtoken':lgtoken,
        'format':"json"
    }