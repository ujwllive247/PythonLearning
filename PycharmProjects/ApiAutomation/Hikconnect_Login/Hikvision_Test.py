import requests
import json


class Login:
    def test_loginPositive(self):
        url = "https://apiiindia.hik-connect.com/v3/users/login/v2"
        headers = {
            "Host": "apiiindia.hik-connect.com",
            "Clienttype": "55",
            "Osversion": "13",
            "Clientversion": "6.3.250.0516",
            "Nettype": "WIFI",
            "Appchannel": "hikvision",
            "Customno": "1000002",
            "Featurecode": "e45fd1d7d67c760f6f7b1f181384fd6e",
            "Sessionid": "",
            "Areaid": "244",
            "Lang": "en-US",
            "Appid": "HikConnect",
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept-Encoding": "gzip, deflate, br",
            "User-Agent": "okhttp/4.10.0"
        }
        data = {
            "account": "918448199695",
            "password": "b71de4a93c840d0e52a4a72c5c926282",
            "featureCode": "e45fd1d7d67c760f6f7b1f181384fd6e",
            "cuName": "c2RrX2dwaG9uZV94ODZfNjQ=",
            "longitude": "",
            "latitude": "",
            "smsToken": "",
            "redirect": "",
            "pushRegisterJson": '[{"channel":99},{"channel":6,"channelRegisterJson":"{\\"token\\":\\"dy0kxELpRXuKHZCdC-4bkH:APA91bEn4USV0PYcfbhJMTOqMbHtNavPztugx9RmljphHmf_Mwnms97-cXbxs7mfC106ZQTmbewZZ0Yab9uLn5IaaWvRwaCp-g0OZ6G1JXq7DR4fVjODKkt0a96l7V7eReQpFK6NUROx\\"}"}]',
            "pushExtJson": '{"language":"default"}'
        }

        response = requests.post(url, headers=headers, data=data)
        response_dict = response.json()

        # Pretty print the response
        pretty_response = json.dumps(response_dict, indent=4)
        print(pretty_response)

        return response_dict


if __name__ == "__main__":
    login_instance = Login()
    login_instance.loginPositive()





class LoginNegative:
    def test_loginNegative(self):
        url = "https://apiiindia.hik-connect.com/v3/users/login/v2"
        headers = {
            "Host": "apiiindia.hik-connect.com",
            "Clienttype": "55",
            "Osversion": "13",
            "Clientversion": "6.3.250.0516",
            "Nettype": "WIFI",
            "Appchannel": "hikvision",
            "Customno": "1000002",
            "Featurecode": "e45fd1d7d67c760f6f7b1f181384fd6e",
            "Sessionid": "",
            "Areaid": "244",
            "Lang": "en-US",
            "Appid": "HikConnect",
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept-Encoding": "gzip, deflate, br",
            "User-Agent": "okhttp/4.10.0"
        }
        data = {
            "account": "918448199695",
            "password": "b71de4a93c840d0e52a4a72c5c926282",
            "featureCode": "e45fd1d7d67c760f6f7b1f181384fd6e",
            "cuName": "c2RrX2dwaG9uZV94ODZfNjQ=",
            "longitude": "",
            "latitude": "",
            "smsToken": "",
            "redirect": "",
            "pushRegisterJson": '[{"channel":99},{"channel":6,"channelRegisterJson":"{\\"token\\":\\"dy0kxELpRXuKHZCdC-4bkH:APA91bEn4USV0PYcfbhJMTOqMbHtNavPztugx9RmljphHmf_Mwnms97-cXbxs7mfC106ZQTmbewZZ0Yab9uLn5IaaWvRwaCp-g0OZ6G1JXq7DR4fVjODKkt0a96l7V7eReQpFK6NUROx\\"}"}]',
            "pushExtJson": '{"language":"default"}'
        }

        response = requests.post(url, headers=headers, data=data)
        response_dict = response.json()

        # Pretty print the response
        pretty_response = json.dumps(response_dict, indent=4)
        print(pretty_response)

        return response_dict


if __name__ == "__main__":
    login_instance = Login()
    login_instance.loginPositive()

