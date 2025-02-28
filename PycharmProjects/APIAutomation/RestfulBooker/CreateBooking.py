# import json
#
# import requests
#
#
# def create_bookings():
#     url = " https://restful-booker.herokuapp.com/booking"
#
#
#     headers = {
#         "Content-Type": "application/json",
#         "Accept":"application/json"
#     }
#
#     payload = {
#       "firstname": "Ujjwal",
#       "lastname": "Thakur",
#        "totalprice": 111,
#       "depositpaid": True,
#       "bookingdates": {
#         "checkin": "2024-02-01",
#         "checkout": "2024-02-07"
#     },
#     "additionalneeds":"Breakfast"
# }
#
#     response = requests.post(url, headers=headers, json=payload)
#     if requests.status_codes == 200 or requests.status_codes ==201:
#        data = response.json()
#        print("Booking Created")
#        print(json.dumps(data, indent=6))
#
# if __name__ == 'main':
#     create_bookings()



import json
import requests

def create_bookings():
    url = "https://restful-booker.herokuapp.com/booking"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    payload = {
        "firstname": "Ujjwal",
        "lastname": "Thakur",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-02-01",
            "checkout": "2024-02-07"
        },
        "additionalneeds": "Breakfast"
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200 or response.status_code == 201:
        data = response.json()
        print("Booking Created")
        print(json.dumps(data, indent=6))
    else:
        print(f"Failed to create booking. Status code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    create_bookings()
