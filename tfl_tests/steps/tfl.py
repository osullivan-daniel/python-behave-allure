from behave import given, when, then
from helpers.common import load_configs, make_request

@given('the user have access to the tfl api')
def step_impl(context):
    data = load_configs('tfl')
    context.app_key = data['app_key']
    context.journeys_url = data['journeys_url']

@when('they travel search for a journey from {search_from} to {search_to}')
def step_impl(context, search_from, search_to):
    url = f"{context.journeys_url}/{search_from}/to/{search_to}?app_key={context.app_key}"
    print(url)
    make_request('GET', url)
    # assert search_from=='A', 'oh crap'
    # print(context.app_key)

@then('they should get a valid result')
def step_impl(context):
    print(context.app_key)
    print(f'okey-doke-so')
    assert 1==2, 'oh crap'
