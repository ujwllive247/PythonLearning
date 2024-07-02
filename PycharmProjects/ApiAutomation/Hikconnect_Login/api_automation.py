

import requests

def get_request(url, headers=None):
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return f"Error: {response.status_code}"

def post_request(url, data, headers=None):
    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 201:
        return response.json()
    else:
        return f"Error: {response.status_code}"

if __name__ == "__main__":
    # Example GET request
    url = "https://jsonplaceholder.typicode.com/posts"
    headers = {"Content-Type": "application/json"}
    print(get_request(url, headers))

    # Example POST request
    url = "https://jsonplaceholder.typicode.com/posts"
    data = {
        "title": "foo",
        "body": "bar",
        "userId": 1
    }
    print(post_request(url, data, headers))
