import json
import requests

#UPDATE example, updates a user's details
api_url = "https://reqres.in/api/users"  
    
def update_data(userId, name, job):
    data = {'name': name, 'job': job}
    response = requests.put(api_url + "/" + userId, data)  #the ID of the record to delete is included on the URL
    if response.status_code == 200: 
        return json.loads(response.content.decode("utf-8"))
    else:
        return None

info = update_data("7","Fred Flintstone","Quality Assurance") #User details passed into function, record to update

#evaluate the service response
if info is not None:
    print('Record updated on {0}'.format(info["updatedAt"]))
else:
    print('[!] UPDATE Request Failed')
