#!/usr/bin/python3
import brownie

# the second argument is whatever you called the variable in conftest.py
# or so I assume
def test_increments(accounts, counter):
    assert counter.getCount() == 0
    counter.increment()
    assert counter.getCount() == 1

