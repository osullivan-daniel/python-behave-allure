import ast
import json
import allure
import operator
import functools

from behave import given, when, then
from helpers.common import load_configs, make_request


@given('the user have access to the tfl api')
def step_impl(context):
    data = load_configs('tfl')
    context.app_key = data['app_key']
    context.journeys_url = data['journeys_url']


@when('they travel search for a journey from {search_from} to {search_to} using ') # Easiest way of handleing an empty mode_of_transport rather than having to try and strip quotes
@when('they travel search for a journey from {search_from} to {search_to} using {mode_of_transport}')
def step_impl(context, search_from, search_to, mode_of_transport=None):

    to_from = f"{search_from}/to/{search_to}"
    # TODO: a function to allow for more optonal params - a dict being passed in the 
    # cucumber table rather than single params is possibly the best way to do it
    optonal = '' if not mode_of_transport else f"mode={mode_of_transport}"
    app_key = f"app_key={context.app_key}"
    
    url = f"{context.journeys_url}/{to_from}?{app_key}" if optonal == '' else f"{context.journeys_url}/{to_from}?{optonal}&{app_key}"

    context.res_code, context.res_content = make_request('GET', url)

    allure.attach(json.dumps(context.res_content, indent=4, sort_keys=True), 'apiResponse.txt')
    # print(json.dumps(context.res_content, indent=4, sort_keys=True))


@then('they should get a valid result')
def step_impl(context):
    # ṃake sure we dont get a client (400's) or a server (500's) errorreturned_mode_of_transport.append
    assert context.res_code < 400, f'Unexpected status code: {context.res_code}'


@then('it should suggest starting points {starting_points}')
def step_impl(context, starting_points):

    expected_starting_points = ast.literal_eval(starting_points)

    returned_starting_locations = []
    for each in context.res_content['fromLocationDisambiguation']['disambiguationOptions']:
        returned_starting_locations.append(each['place']['commonName'])

    # Ẹnsure that all the points were expecting are returned ignoring others that may be there
    assert set(expected_starting_points).issubset(returned_starting_locations), f'Not all of the expected locatons were found. Expected: {expected_starting_points}, Found: {returned_starting_locations}'

    # Ạlternativly we could assert they match exactly - would depend on the requirments
    assert set(returned_starting_locations) == set(expected_starting_points), f'Expected does not match found exactly. Expected: {expected_starting_points}, Found: {returned_starting_locations}'


# TODO:: it should suggest starting points & it should suggest mode of transport are very similar a common functon should be lookied into
@then('it should suggest mode of transport {expected_mode_of_transport}')
def step_impl(context, expected_mode_of_transport):

    expected_mode_of_transport = ast.literal_eval(expected_mode_of_transport)

    returned_mode_of_transport = []
    for each in context.res_content['toLocationDisambiguation']['disambiguationOptions']:
        if 'modes' in each['place']:
            returned_mode_of_transport.append(each['place']['modes'])

    # latten list of lists
    returned_mode_of_transport = functools.reduce(operator.iconcat, returned_mode_of_transport, [])

    # Ẹnsure that all the points were expecting are returned ignoring others that may be there
    assert set(expected_mode_of_transport).issubset(returned_mode_of_transport), f'Not all of the expected locatons were found. Expected: {expected_mode_of_transport}, Found: {returned_mode_of_transport}'

    # Ạlternativly we could assert they match exactly - would depend on the requirments
    # assert set(expected_mode_of_transport) == set(returned_mode_of_transport), f'Expected does not match found exactly. Expected: {expected_mode_of_transport}, Found: {returned_mode_of_transport}'
