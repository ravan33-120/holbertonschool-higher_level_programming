#!/usr/bin/python3
"""
Module: task_02_csv
Author: Your Name
Description:
    This module provides functionality to convert CSV data into JSON format.
    It reads a CSV file using DictReader, converts the rows into a list of
    dictionaries, and stores the result in data.json.
"""

import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Convert a CSV file into JSON format and save the result as data.json.

    Args:
        csv_filename (str): The path to the input CSV file.

    Returns:
        bool: True if the conversion is successful, False otherwise.

    Behavior:
        - Reads data from a CSV file.
        - Converts each row to a dictionary using csv.DictReader.
        - Serializes the list of dictionaries into JSON.
        - Writes the JSON output to a file named data.json.
        - Handles exceptions such as missing files.
    """
    try:
        data_list = []

        # Open and read CSV file
        with open(csv_filename, "r", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)

            # Append each row (as a dictionary) into the list
            for row in reader:
                data_list.append(row)

        # Write JSON output to data.json
        with open("data.json", "w", encoding="utf-8") as jsonfile:
            json.dump(data_list, jsonfile, indent=4)

        return True

    except Exception:
        return False

