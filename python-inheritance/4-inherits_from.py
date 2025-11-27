#!/usr/bin/python3
"""Module that defines inherits_from function."""


def inherits_from(obj, a_class):
    """
    Returns True if obj is an instance of a class that
    inherited (directly or indirectly) from a_class.
    Otherwise False.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
