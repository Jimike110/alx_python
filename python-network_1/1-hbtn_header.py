#!/usr/bin/python3
"""
1-hbtn_header.py - A script to fetch and display the value of the variable X-Request-Id in the response header.
"""

import requests
import sys

if __name__ == "__main__":
    # Check if a URL is provided as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: ./1-hbtn_header.py <URL>")
        sys.exit(1)

    # Get the URL from the command-line argument
    url = sys.argv[1]

    # Send a GET request to the specified URL
    response = requests.get(url)

    # Display the value of X-Request-Id if present in the response header
    x_request_id = response.headers.get('X-Request-Id')
    if x_request_id:
        print(x_request_id)
