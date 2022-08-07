## IMPORTANT
This repo is automatically cloned when starting the docker container in python-behave-allure-docker  
  
## app_key
Acording to the tfl webaite you will need to register with tfl and generate a key - https://api.tfl.gov.uk/ however i have seen it work without a key.... 
(I've told them so they will probably fix it at some point)  
That said the code is setup to require one so pleasse follow the instructons below to set one up for yourself

Once registered:  
    - Go to 'Products' along the top main bar  
    - Select '500 Requests per min'  
    - Then type a name into the box just under 'Your subscriptions'  
    - and press the 'Subscribe' button  
    - Then go to 'Profile' along the top main bar  
    - Copy your 'Primary key' and replace the string 'PUT_YOUR_APP_KEY_HERE' in your 'configs/env.json'  


## The Tests
Note one of the tfl tests fails. This is intentonal. As the test requests a journey by bus and only one by rail is returned the test fails. The returned json makes no mention of it being an alternative so to me that sounds like a fail on the face of without discussing the ratonal behind it working like this.