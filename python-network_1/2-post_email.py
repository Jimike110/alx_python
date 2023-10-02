#!/usr/bin/python3
"""
2-post_email.py - A script to send a POST request to a URL with an email as a parameter and display the response body.
"""

import requests
import sys

if __name__ == "__main__":
    # Check if both URL and email are provided as command-line arguments
    if len(sys.argv) != 3:
        print("Usage: ./2-post_email.py <URL> <email>")
        sys.exit(1)

    # Get the URL and email from the command-line arguments
    url = sys.argv[1]
    email = sys.argv[2]

    # Define the payload with the email parameter
    payload = {'email': email}

    # Send a POST request to the specified URL with the payload
    response = requests.post(url, data=payload)

    # Display the body of the response
    print(response.text)
