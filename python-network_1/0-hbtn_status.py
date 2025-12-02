#!/usr/bin/python3
from urllib import request

url = "https://intranet.hbtn.io/status"

with request.urlopen(url) as response:
    body = response.read()

print("Body response:")
print("    - type: {}".format(type(body)))
print("    - content: {}".format(body))
print("    - utf8 content: {}".format(body.decode("utf-8")))
