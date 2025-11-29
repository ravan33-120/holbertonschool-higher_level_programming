#!/usr/bin/python3
"""
Module: task_03_xml
Description:
    Provides serialization and deserialization of Python dictionaries using XML.
    Uses xml.etree.ElementTree from Python's standard library.
"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary into XML format and write it to a file.

    Args:
        dictionary (dict): The dictionary to serialize into XML.
        filename (str): The filename where the XML will be saved.

    Returns:
        bool: True if serialization succeeds, False otherwise.
    """
    try:
        # Create root element <data>
        root = ET.Element("data")

        # Create child elements from dictionary key/value pairs
        for key, value in dictionary.items():
            child = ET.SubElement(root, key)
            child.text = str(value)   # XML stores everything as text

        # Build the tree and write to file
        tree = ET.ElementTree(root)
        tree.write(filename, encoding="utf-8", xml_declaration=True)

        return True

    except Exception:
        return False


def deserialize_from_xml(filename):
    """
    Deserialize XML data from a file and convert it back into a dictionary.

    Args:
        filename (str): The path to the XML file.

    Returns:
        dict or None: Dictionary with the XML data, or None if an error occurs.
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        result = {}

        # Iterate through child elements
        for child in root:
            result[child.tag] = child.text  # type = string (XML limitation)

        return result

    except Exception:
        return None

