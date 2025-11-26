#!/usr/bin/python3
"""Module that defines the MyList class which stores and prints sorted values."""


class MyList(list):
    """Custom list class that stores values and can print them sorted."""

    def __init__(self):
        """Initialize the custom list storage."""
        self.ourlist = []

    def append(self, value):
        """Add a value to the custom list."""
        self.ourlist += [value]

    def print_sorted(self):
        """Print the list sorted in ascending order without modifying it."""
        print(sorted(self.ourlist))

    def __str__(self):
        """Return the string representation of the list."""
        return str(self.ourlist)
