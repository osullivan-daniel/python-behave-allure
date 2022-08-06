## IMPORTANT
This repo is automatically cloned when starting the docker container in python-behave-allure-docker

## app_key
You will need to register with tfl and generate a key - https://api.tfl.gov.uk/

Once registered:
    - Go to 'Products' along the top main bar
    - Select '500 Requests per min'
    - Then type a name into the box just under 'Your subscriptions'
    - and press the 'Subscribe' button 
    - Then go to 'Profile' along the top main bar
    - Copy your 'Primary key' and replace the string 'PUT_YOUR_APP_KEY_HERE' in your 'configs/env.json'