"""
test_kostky.py

test pro prográmek kostky.py
"""
from os import path
import sys
sys.path.append(path.join(path.dirname(__file__), '..'))


import kostky
import pytest

def test_add():
    assert kostky.add(7, 3) == 10
    assert kostky.add(7) == 9
    assert kostky.add(5) == 7

def test_product():
    assert kostky.product(5, 5 ) == 25
    assert kostky.product(5) == 10
    assert kostky.product(7) == 14

def test_add_strings():
    result = kostky.add("Hello", " World")
    assert result == "Hello World"
    assert type(result) is str
    assert "Hedlo" not in result

def test_product_strings():
    assert kostky.product("Hello ", 3) == "Hello Hello Hello "
    result = kostky.product("Hello ")
    assert result == "Hello Hello "
    assert type(result) is str
    
def test_add_float():
    result = kostky.add(10.5, 25.5)
    assert result == 36

# parametrizace testů
@pytest.mark.parametrize("num1, num2, result",
                        [
                            (7, 3, 10), 
                            (7, 2, 9), 
                            (5, 2, 7), 
                            ("Hello", " World", "Hello World"), 
                            (10.5, 25.5, 36), 
                            (15.82, 3.1, 18.92)
                        ]
                        )
def test_addVSE(num1, num2, result):
    assert kostky.add(num1, num2) == result
  
