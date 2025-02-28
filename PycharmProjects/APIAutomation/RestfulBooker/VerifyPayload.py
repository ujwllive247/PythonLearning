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

        # Extract booking ID from response
        booking_id = data["bookingid"]


        # Verify the created booking
        verify_booking(booking_id, payload)
    else:
        print(f"Failed to create booking. Status code: {response.status_code}")
        print(response.text)

def verify_booking(booking_id, original_payload):
    url = f"https://restful-booker.herokuapp.com/booking/{booking_id}"
    headers = {
        "Accept": "application/json"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        booking_data = response.json()
        print("Booking Details:")
        print(json.dumps(booking_data, indent=6))

        # Check if the booking data matches the original payload
        is_match = (booking_data["firstname"] == original_payload["firstname"] and
                    booking_data["lastname"] == original_payload["lastname"] and
                    booking_data["totalprice"] == original_payload["totalprice"] and
                    booking_data["depositpaid"] == original_payload["depositpaid"] and
                    booking_data["bookingdates"]["checkin"] == original_payload["bookingdates"]["checkin"] and
                    booking_data["bookingdates"]["checkout"] == original_payload["bookingdates"]["checkout"] and
                    booking_data["additionalneeds"] == original_payload["additionalneeds"])

        if is_match:
            print("Booking verification successful: The fetched booking data matches the original payload.")
        else:
            print("Booking verification failed: The fetched booking data does not match the original payload.")
    else:
        print(f"Failed to fetch booking details. Status code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    create_bookings()
