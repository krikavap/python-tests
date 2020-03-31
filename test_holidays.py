"""
test_holidays.py

"""
from os import path
import sys
sys.path.append(path.join(path.dirname(__file__), '..'))

import pytest
import isholiday

@pytest.mark.parametrize("year", (2015, 2016, 2020, 1999, 2033, 2048))

def test_xmas_2016(year):
    holidays = isholiday.getholidays(year)
    assert(28, 10) in holidays