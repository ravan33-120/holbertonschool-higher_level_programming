#!/usr/bin/python3
"""
This module defines the Student class with JSON serialization and
deserialization capabilities.
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

    def to_json(self, attrs=None):
        """
        Return a dictionary representation of the Student instance.

        If attrs is a list of strings, only attributes whose names appear
        in this list are included in the returned dictionary.

        Args:
            attrs (list, optional): List of attribute names to include.

        Returns:
            dict: Dictionary of selected or all attributes.
        """
        if isinstance(attrs, list):
            return {key: self.__dict__[key]
                    for key in attrs if key in self.__dict__}
        return self.__dict__

    def reload_from_json(self, json):
        """
        Replace all attributes of the Student instance using a dictionary.

        Args:
            json (dict): Dictionary where keys are attribute names and
                         values are the values to set.

        Each key corresponds to a public attribute of the class.
        """
        for key, value in json.items():
            setattr(self, key, value)
