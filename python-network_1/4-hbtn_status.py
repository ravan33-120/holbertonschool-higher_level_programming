#!/usr/bin/python3
"""Fetches https://intranet.hbtn.io/status using the requests package.

Usage: ./4-hbtn_status.py
"""
import requests


if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"

    response = requests.get(url)
    content = response.text

    print("Body response:")
    print("    - type: {}".format(type(content)))
    print("    - content: {}".format(content))
