#!/usr/bin/python3
"""
This module provides a function that writes a string to a UTF-8
encoded text file and returns the number of characters written.
"""


def write_file(filename="", text=""):
    """
    Write a string to a UTF-8 text file and return the number of characters.

    The file is created if it does not exist and overwritten if it does.

    Args:
        filename (str): Name of the file to write to.
        text (str): The string content to write.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
