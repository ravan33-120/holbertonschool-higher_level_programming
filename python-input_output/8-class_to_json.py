#!/usr/bin/python3
"""
This module provides a function that returns the dictionary description
of an object's attributes for JSON serialization.
"""


def class_to_json(obj):
    """
    Return the dictionary representation of an object's attributes.

    Args:
        obj: An instance of a class with JSON-serializable attributes
             (list, dict, string, integer, boolean).

    Returns:
        dict: A dictionary containing the object's attributes.
    """
    return obj.__dict__
