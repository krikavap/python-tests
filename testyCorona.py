"""
testyCorona.py


"""

import json

class TestyCorona_json:
    def __init__(self):
        self.__data = None

    def connect(self, data_file):
        with open(data_file) as json_file:
            self.__data = json.load(json_file)


    def nacti_data(self, datum):
        for den in self.__data["data"]:
            if den["datum"] == datum:
                return den
            
    def close(self):
        pass