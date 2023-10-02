#!/usr/bin/python3
"""
5-json_api.py - A script to send a POST request and handle JSON response.
"""

import requests
import sys

if __name__ == "__main__":
    # Set the default value for the letter parameter
    q = "" if len(sys.argv) == 1 else sys.argv[1]

    # URL for the POST request
    url = "http://0.0.0.0:5000/search_user"

    # Send a POST request with the letter as a parameter
    response = requests.post(url, data={'q': q})

    try:
        # Parse the JSON response
        json_data = response.json()

        # Check if the JSON is not empty
        if json_data:
            print("[{}] {}".format(json_data.get('id'), json_data.get('name')))
        else:
            print("No result")

    except ValueError:
        # Handle invalid JSON
        print("Not a valid JSON")
