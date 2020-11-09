import json
import requests

#DELETE example, deletes a user from the list
api_url = "https://reqres.in/api/users"  
    
def delete_data(userId):
    response = requests.delete(api_url + "/" + userId)  #the ID of the record to delete is included on the URL
    if response.status_code == 204: #https://httpstatuses.com/204
        return "Record Deleted"
    else:
        return None

info = delete_data("7") #User Id passed into function

#evaluate the service response
if info is not None:
    print(info)
else:
    print('[!] DELETE Request Failed')
