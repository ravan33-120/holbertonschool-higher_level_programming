#!/usr/bin/python3
"""Module that defines the Rectangle class based on BaseGeometry."""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class that inherits from BaseGeometry."""

    def __init__(self, width, height):
        """Initialize Rectangle with validated width and height."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Returns the area of the Rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Returns the rectangle description [Rectangle] width/height."""
        return f"[Rectangle] {self.__width}/{self.__height}"
