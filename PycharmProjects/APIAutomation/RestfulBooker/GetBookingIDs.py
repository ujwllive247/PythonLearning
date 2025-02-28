import json

import requests


def get_booking_ids():
    url = "https://restful-booker.herokuapp.com/booking"


    headers = {
        "Content-Type": "application/json"
    }

    response = requests.get(url, headers=headers)

    if response.status_code==200:
        data = response.json()
        print("Below, is the booking Ids")
        # Printing the response...........
        print(json.dumps(data, indent=6))

if __name__ == "__main__":
    get_booking_ids()