#!/usr/bin/python3

"""
Fetches https://alx-intranet.hbtn.io/status

Requirements:
    - You must use the package requests
    - You are not allow to import packages other than requests
    - The body of the response must be display
      like the following example (tabulation before -)
"""

if __name__ == '__main__':
    from requests import get

    r = get('https://alx-intranet.hbtn.io/status')
    print('Body response:')
    print(f'\t- type: {type(r.text)}')
    print(f'\t- content: {r.text}')
