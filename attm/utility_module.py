"""This module contains the utility functions for the flask application.
The functions in this module are helper functions to support the
features of the flask application. This module imports other modules
from Python's standard library, including: datetime, math, operator and time.
"""

def traverse_json(json_object, result, index=0):
    if 'name' in json_object:
        result.append({"name": json_object['name'], "index": index, "score": 0})
        index += 1
    if 'children' in json_object:
        for child in json_object['children']:
            index = traverse_json(child, result, index)
    return index