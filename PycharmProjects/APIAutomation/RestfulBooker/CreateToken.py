import token
from os import name

import requests
import json
import unittest



import requests

def authenticate():
    # API endpoint
    url = "https://restful-booker.herokuapp.com/auth"

    # Headers
    headers = {
        "Content-Type": "application/json"
    }

    # Request body
    payload = {
        "username": "admin",
        "password": "password123"
    }

    # Sending POST request
    response = requests.post(url, headers=headers, json=payload)

    # Checking response status code
    if response.status_code == 200:
        # Parsing JSON response
        data = response.json()
        print("Authentication successful!")
        print("Token:", data.get("token"))
    else:
        print("Authentication failed!")
        print("Status code:", response.status_code)
        print("Response:", response.text)

if __name__ == "__main__":
    authenticate()











