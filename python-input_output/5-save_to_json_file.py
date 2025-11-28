#!/usr/bin/python3
"""
This module provides a function that writes a Python object to a file
in its JSON string representation.
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Write a Python object to a file using JSON representation.

    Args:
        my_obj: The Python object to serialize.
        filename (str): The name of the file to write to.

    The function does not handle serialization or file permission errors.
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
