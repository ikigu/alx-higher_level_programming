#!/usr/bin/python3

"""
Takes in a URL, sends a request to the URL
and displays the value of the X-Request-Id variable
found in the header of the response.

Requirements:
    - You must use the packages requests and sys
    - You are not allowed to import packages other than reqiests and sys
    - The value of this variable is different for each request
    - You don’t need to check arguments passed to the script (number or type)
"""

if __name__ == '__main__':
    import requests
    import sys

    URL = sys.argv[1]

    r = requests.get(URL)

    if r.ok:
        try:
            print(r.headers['X-Request-Id'])
        except KeyError:
            pass
