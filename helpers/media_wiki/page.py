import json
import conftest

from data.page import get_all_pages, get_by_page_id

def post_page(sesh, page: json):
    full_url = f"{conftest.mediawiki_config['base_url']}{conftest.mediawiki_config['api_end_point']}"

    return sesh.post(url=full_url, data=page)


def search_wiki_pages(sesh, search: str):
    full_url = f"{conftest.mediawiki_config['base_url']}{conftest.mediawiki_config['api_end_point']}"
    search_params = get_all_pages(search)

    return sesh.get(url=full_url, params=search_params)

def get_wiki_page(sesh, page_id: str):
    full_url = f"{conftest.mediawiki_config['base_url']}{conftest.mediawiki_config['api_end_point']}"
    search_params = get_by_page_id(page_id)

    return sesh.get(url=full_url, params=search_params)
