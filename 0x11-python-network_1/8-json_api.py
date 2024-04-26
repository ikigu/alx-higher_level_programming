#!/usr/bin/python3

"""
Write a Python script that takes in a letter
and sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.

Requirements:
    - The letter must be sent in the variable q
    - If no argument is given, set q=""
    - If the response body is properly JSON formatted
      and not empty, display the id and name like this: [<id>] <name>
    - Otherwise:
        - Display Not a valid JSON if the JSON is invalid
        - Display No result if the JSON is empty
    - You must use the package requests and sys
    - You are not allowed to import packages other than requests and sys
"""

if __name__ == '__main__':
    import sys
    import requests

    params = {'q': ""}

    if len(sys.argv) == 2:
        params['q'] = sys.argv[1]

    url = 'http://0.0.0.0/search_user'

    response = requests.post(url, params=params)

    try:
        resp_content = response.json()
    except ValueError:
        print("Not a valid JSON")

    if len(resp_content) == 0:
        print("No result")
    else:
        print(f'[{resp_content["id"]}] {resp_content["name"]}')
