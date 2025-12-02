#!/usr/bin/python3
"""Sends a POST request to search for a user by a letter.

Usage: ./8-json_api.py <letter>
"""
import sys
import requests


if __name__ == "__main__":
    # If no argument is given, q = ""
    q = sys.argv[1] if len(sys.argv) > 1 else ""

    url = "http://0.0.0.0:5000/search_user"
    data = {"q": q}

    try:
        response = requests.post(url, data=data)
        json_data = response.json()
    except ValueError:
        print("Not a valid JSON")
        sys.exit(0)

    # If JSON is empty
    if not json_data:
        print("No result")
    else:
        print("[{}] {}".format(json_data.get("id"), json_data.get("name")))
