from helpers.common import load_configs

mediawiki_config = None

def pytest_configure():
    global mediawiki_config
    mediawiki_config = load_configs('mediawiki')
