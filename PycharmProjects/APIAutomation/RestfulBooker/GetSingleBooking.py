import json
import requests
def get_single_booking():
    url = "https://restful-booker.herokuapp.com/booking/4207"
    headers = {
        "Accept": "application/json",
        "Content-Type":"application/json"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        print("This is your retrieved ID details")
        print(json.dumps(data, indent=6))
    else:
        print(f"ID not found in the database. Status code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    get_single_booking()

