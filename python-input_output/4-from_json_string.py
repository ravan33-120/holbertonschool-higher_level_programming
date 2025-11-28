#!/usr/bin/python3
"""
This module provides a function that converts a JSON string into the
corresponding Python data structure.
"""

import json


def from_json_string(my_str):
    """
    Convert a JSON-formatted string into a Python object.

    Args:
        my_str (str): A string representing a JSON structure.

    Returns:
        Any: The Python object resulting from parsing the JSON string.
    """
    return json.loads(my_str)
