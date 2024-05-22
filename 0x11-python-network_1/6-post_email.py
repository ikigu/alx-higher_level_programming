#!/usr/bin/python3

"""
Write a Python script that takes in a URL and an email address,
sends a POST request to the passed URL with the email
as a parameter, and displays the body of the response

Requirements:
    - The email must be sent in the email variable
    - You must use the packages requests and sys
    - You are not allowed to import packages other than requests and sys
    - You don't need to check arguments passed to the script (number or type)
"""

if __name__ == '__main__':
    import sys
    import requests

    url = sys.argv[1]
    email = sys.argv[2]

    payload = {'email': email}

    r = requests.post(url, data=payload)
    print(r.text)
