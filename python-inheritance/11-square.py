#!/usr/bin/python3
"""Module that defines the Square class based on Rectangle."""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle."""

    def __init__(self, size):
        """Initialize Square with validated size."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Returns the area of the Square."""
        return self.__size * self.__size

    def __str__(self):
        """Returns the square description [Square] size/size."""
        return f"[Square] {self.__size}/{self.__size}"
