#!/usr/bin/python3
"""
This module provides a function that converts a Python object into its
JSON string representation.
"""

import json


def to_json_string(my_obj):
    """
    Return the JSON representation of a Python object as a string.

    Args:
        my_obj: Any serializable Python object (list, dict, int, str, etc.).

    Returns:
        str: JSON-formatted string representation of the object.
    """
    return json.dumps(my_obj)
