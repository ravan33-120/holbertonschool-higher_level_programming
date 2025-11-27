#!/usr/bin/python3
"""Module that defines the MyList class."""


class MyList(list):
    """Class that inherits from list and adds a sorted print method."""

    def print_sorted(self):
        """Prints the list sorted in ascending order."""
        print(sorted(self))
