#!/usr/bin/python3
"""Module that defines the BaseGeometry class."""


class BaseGeometry:
    """BaseGeometry class with public instance method area."""

    def area(self):
        """Raises an exception because area is not implemented."""
        raise Exception("area() is not implemented")
