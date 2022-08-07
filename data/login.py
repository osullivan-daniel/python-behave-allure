def gen_login_parms(user: str, password: str, lgtoken:str):
    return {
        'action':"login",
        'lgname': user,
        'lgpassword':password,
        'lgtoken':lgtoken,
        'format':"json"
    }