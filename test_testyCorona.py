"""
test_testyCorona.py

"""

from os import path
import sys
sys.path.append(path.join(path.dirname(__file__), '..'))

from testyCorona import TestyCorona_json
#import pytest

db = None   # iniciace proměnné

def setup_module(module):
    """
    připojení db (iniciace). provede se jen na začátku celého testu
    """
    print("\n--------------setup----------------")
    global db       # db je nadefinována jako globální
    db = TestyCorona_json()
    db.connect("testy.json")

def teardown_module(module):
    """
    ukončení připojení a uvolnění prostředků
    """
    print("\n--------------close----------------")
    db.close()

def test_prvniData():
    prvniData = db.nacti_data("27.1.2020")
    assert prvniData["datum"] == "27.1.2020"
    assert prvniData["testy-den"] == 20
    assert prvniData["testy-celkem"] == 20


def test_druhyData():
    prvniData = db.nacti_data("28.1.2020")
    assert prvniData["datum"] == "28.1.2020"
    assert prvniData["testy-den"] == 8
    assert prvniData["testy-celkem"] == 28