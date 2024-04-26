#!/usr/bin/python3
"""
Write a Python script that takes your GitHub credentials
(username and password) and uses the GitHub API to display your id

"""

if __name__ == "__main__":
    import requests
    import sys

    repo = sys.argv[1]
    owner = sys.argv[2]

    headers = {'Accept': 'application/vnd.github+json'}

    params = {'per_page': 10, 'page': 1}

    response = requests.get(
        f'https://api.github.com/repos/{owner}/{repo}/commits',
        headers=headers, params=params)

    if response.ok:
        response = response.json()

        for i in range(0, 10):

            sha_code = response[i]["sha"]
            author = response[i]["commit"]["author"]["name"]

            print(
                f'{sha_code}: {author}')
    else:
        print(None)
