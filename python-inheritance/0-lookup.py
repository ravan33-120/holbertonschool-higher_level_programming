#!/usr/bin/python3
"""Module that defines the function lookup, which returns list of attributes and methods"""

def lookup(obj):
    """Returns the list of available attributes and methods of an object"""
    return dir(obj)
