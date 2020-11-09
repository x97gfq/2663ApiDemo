import json
import requests

#GET example, returns list of Users
#this is an example of a program calling an API ('GET Request'), return all records (likely from a database table)
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
        print(' {0} {1}  {2}'.format(firstname, lastname, email))
else:
    print('[!] GET Request Failed')
