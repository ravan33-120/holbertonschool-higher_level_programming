#!/usr/bin/python3
"""Fetches a URL and displays its body (decoded in UTF-8).

Handles HTTPError exceptions and prints:
Error code: <HTTP status code>

Usage: ./3-error_code.py <URL>
"""
import sys
import urllib.error
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)

    try:
        with urllib.request.urlopen(request) as response:
            print(response.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
