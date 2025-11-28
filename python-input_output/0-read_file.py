#!/usr/bin/python3
"""
This module provides a function to read a UTF-8 encoded text file
and print its contents to standard output.
"""


def read_file(filename=""):
    """
    Print the contents of a UTF-8 text file to stdout.

    Args:
        filename (str): The name of the file to read.
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
