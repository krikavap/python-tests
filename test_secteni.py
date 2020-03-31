"""
test_secteni.py

"""

from os import path
import sys
sys.path.append(path.join(path.dirname(__file__), '..'))

from secteni import secti


def test_secti():
    assert secti(1, 2) == 3

