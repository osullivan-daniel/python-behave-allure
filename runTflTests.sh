#!/bin/bash

source ~/.profile

# Run tfl tests
behave tests/test_tfl/ --no-capture --no-capture-stderr