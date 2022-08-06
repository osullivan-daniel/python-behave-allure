from behave   import given, when, then

@given('the user have access to the tfl api')
def step_impl(context):
    # context.api_key=
    pass

@when('they travel search for a journey from {search_from} to {search_to}')
def step_impl(context, search_from, search_to):
    print(search_from)
    assert search_from=='A', 'oh crap'

@then('they should get a valid result')
def step_impl(context):
    print(f'okey-doke-so')
    assert 1==2, 'oh crap'