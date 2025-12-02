#!/usr/bin/python3
"""Uses the GitHub API to display the user's id.

Usage: ./10-my_github.py <username> <token>
"""
import sys
import requests


if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]

    url = "https://api.github.com/user"

    response = requests.get(url, auth=(username, token))
    json_data = response.json()

    print(json_data.get("id"))
