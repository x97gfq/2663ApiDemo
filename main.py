import json
import requests

#Example of a program consuming an Open Data API
#Info: https://data.novascotia.ca/Crime-and-Justice/Crime-Statistics-Crime-Severity-Index/w64p-5ue3
#Public API: https://data.novascotia.ca/resource/w64p-5ue3.json
#The API returns all records, so we'll only print out records where the property 'geography' contains the search_term

api_url = "https://data.novascotia.ca/resource/w64p-5ue3.json"
search_term = "Barrington"

def get_data():
    response = requests.get(api_url)
    if response.status_code == 200:
        return json.loads(response.content.decode("utf-8"))
    else:
        return None

info = get_data()

if info is not None:
    print("Results for " + search_term + ":")
    for item in info:
        if (item["geography"].find(search_term) != -1):
            print(item["year"][:4] + " severity index: " + item["total_crime_severity_index"])
else:
    print('[!] Request Failed')
