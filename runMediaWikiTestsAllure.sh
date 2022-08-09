#!/bin/bash
source ~/.profile
 
# Remove existing results
rm -rf mediawiki_results

# Run mediawiki tests
pytest --alluredir mediawiki_results 

allure serve mediawiki_results