#!/usr/bin/python3
"""
6-my_github.py - A script to access GitHub API and display user id.
"""

import requests
import sys

if __name__ == "__main__":
    # Check if both username and personal access token are provided
    if len(sys.argv) != 3:
        print("Usage: {} <username> <personal_access_token>".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    token = sys.argv[2]

    # URL for the GitHub API to get user information
    url = "https://api.github.com/user"

    # Set up the authentication using Basic Authentication with personal access token
    auth = (username, token)

    # Send a GET request to the GitHub API
    response = requests.get(url, auth=auth)

    try:
        # Parse the JSON response
        user_data = response.json()

        # Display the user id
        print(user_data.get('id'))

    except ValueError:
        # Handle invalid JSON
        print("None")
