#!/usr/bin/python3
"""
This module provides a function that appends a string to the end of a
UTF-8 encoded text file and returns the number of characters added.
"""


def append_write(filename="", text=""):
    """
    Append a string to the end of a UTF-8 text file.

    If the file does not exist, it will be created automatically.
    The function returns the number of characters written.

    Args:
        filename (str): The name of the file to append to.
        text (str): The content to append to the file.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
