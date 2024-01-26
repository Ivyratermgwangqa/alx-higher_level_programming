#!/usr/bin/python3
"""
Takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user with the letter as a parameter using requests.
"""

import requests
import sys

if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    data = {'q': letter}

    response = requests.post(url, data=data)
    
    try:
        user_dict = response.json()
        if user_dict:
            print("[{}] {}".format(user_dict.get('id'), user_dict.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
