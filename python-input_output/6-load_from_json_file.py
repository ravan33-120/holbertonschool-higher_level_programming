#!/usr/bin/python3
"""
This module provides a function that loads a Python object from a JSON file.
"""

import json


def load_from_json_file(filename):
    """
    Load and return a Python object from a JSON file.

    Args:
        filename (str): The path to the JSON file.

    Returns:
        Any: The Python object represented by the JSON file's content.

    The function does not handle JSON decoding errors or file permission
    exceptions, as required by the project specifications.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
