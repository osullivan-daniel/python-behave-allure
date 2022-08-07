#!/bin/bash
source ~/.profile

# Remove existing results
rm -rf tfl_results

# Run tfl tests
behave -f allure_behave.formatter:AllureFormatter -o tfl_results tests/test_tfl/

allure serve tfl_results