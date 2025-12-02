#!/usr/bin/python3
"""Sends a POST request to a given URL with an email parameter.

Usage: ./6-post_email.py <URL> <email>
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    data = {"email": email}

    response = requests.post(url, data=data)
    print(response.text)
