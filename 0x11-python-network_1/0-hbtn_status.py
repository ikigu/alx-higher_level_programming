#!/usr/bin/python3

"""
fetches https://alx-intranet.hbtn.io/status
"""

if __name__ == "__main__":
    import urllib.request

    url = 'https://alx-intranet.hbtn.io/status'

    with urllib.request.urlopen(url) as response:
        response_data = response.read()
        print('Body response:')
        print(f'\t- type: {type(response_data)}')
        print(f'\t- content: {response_data}')
        print(f'\t- utf8 content: {response_data.decode("utf8")}')
