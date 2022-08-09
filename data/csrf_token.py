def csrf_token_params():
    return {
            "action": "query",
            "meta": "tokens",
            "format": "json"
        }