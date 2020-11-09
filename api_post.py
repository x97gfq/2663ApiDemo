import json
import requests

#POST example (POST new JSON data to create a new record)
api_url = "https://reqres.in/api/users"

def post_data(name, job):
    data = {'name': name, 'job': job}
    response = requests.post(api_url, data)
    if response.status_code == 201: #https://httpstatuses.com/201 'Created' status code
        return json.loads(response.content.decode("utf-8"))
    else:
        return None

info = post_data("Fred Flintstone", "Software Engineer")

#evaluate the service response
if info is not None: 
    id = info["id"]
    createdAt = info["createdAt"]
    print('New Record {0} added on {1}'.format(id, createdAt))
else:
    print('[!] Failed to add new record')
