def page_base_fields(csrf_token):
    return {
            "action": "edit",
            "token": csrf_token,
            "format": "json",
        }

def get_all_pages(search_param):
    return {
        "action": "query",
        "list": "allpages",
        "apfrom": search_param,
        "format": "json",
    }
     
def get_by_page_id(page_id):
    return {
        "action": "parse",
        "pageid": page_id,
        "format": "json",
    }
