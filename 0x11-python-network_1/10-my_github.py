#!/usr/bin/python3
"""
Takes your GitHub credentials (username and password) and uses the GitHub API to display your id using requests.
"""

import requests
import sys

if __name__ == "__main__":
    url = 'https://api.github.com/user'
    username = sys.argv[1]
    password = sys.argv[2]

    response = requests.get(url, auth=(username, password))
    
    try:
        user_info = response.json()
        print(user_info.get('id'))
    except ValueError:
        print(None)
