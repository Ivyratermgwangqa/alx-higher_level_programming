#!/usr/bin/python3
"""
List 10 commits (from the most recent to oldest) of the repository “rails” by the user “rails” using the GitHub API.
"""

import requests
import sys

if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(owner, repo)

    response = requests.get(url)

    for commit in response.json()[:10]:
        sha = commit.get('sha')
        author_name = commit.get('commit').get('author').get('name')
        print("{}: {}".format(sha, author_name))
