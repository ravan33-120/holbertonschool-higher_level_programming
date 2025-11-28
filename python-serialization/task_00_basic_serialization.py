#!/usr/bin/python3
# task_00_basic_serialization.py

import json

def serialize_and_save_to_file(data, filename):
    """Serialize a Python dictionary to JSON and save it to a file."""
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)  # indent=4 → JSON-u gözəl formatda yazır


def load_and_deserialize(filename):
    """Load JSON data from a file and deserialize it into a Python dictionary."""
    with open(filename, "r") as file:
        data = json.load(file)
    return data
