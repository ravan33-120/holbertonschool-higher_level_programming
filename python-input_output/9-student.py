#!/usr/bin/python3
"""
This module defines the Student class with basic attributes and a method
to return its dictionary representation for JSON serialization.
"""


class Student:
    """
    Represents a student with a first name, last name, and age.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initialize the Student instance.

        Args:
            first_name (str): The student's first name.
            last_name (str): The student's last name.
            age (int): The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Return the dictionary representation of the Student instance.

        Returns:
            dict: A dictionary containing the student's attributes.
        """
        return self.__dict__
