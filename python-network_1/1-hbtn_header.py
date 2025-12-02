#!/usr/bin/python3
import sys
from urllib import request

if __name__ == "__main__":
    url = sys.argv[1]

    with request.urlopen(url) as response:
        x_request_id = response.headers.get("X-Request-Id")

    print(x_request_id)
