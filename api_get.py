import json
import requests

#GET example, returns list of Users
api_url = "https://reqres.in/api/users"

def get_data():
    response = requests.get(api_url)
    if response.status_code == 200:
        return json.loads(response.content.decode("utf-8"))
    else:
        return None

info = get_data()

#evaluate the service response
if info is not None:
    for item in info["data"]:
        email = item["email"]
        firstname = item["first_name"]
        lastname = item["last_name"]
        print('Firstname: {0} Lastname: {1} Email {2}'.format(firstname, lastname, email))
else:
    print('[!] GET Request Failed')
