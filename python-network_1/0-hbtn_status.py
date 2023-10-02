#!/usr/bin/python3
"""
0-hbtn_status.py - A script to fetch and display the status of https://alu-intranet.hbtn.io
"""

import requests

if __name__ == "__main__":
    # URL to fetch
    url = "https://alu-intranet.hbtn.io/status"

    # Send GET request to the URL
    response = requests.get(url)

    # Display information about the response
    print("Body response:")
    print("\t- type:", type(response.text))
    print("\t- content:", response.text)
