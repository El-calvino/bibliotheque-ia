import requests 


response = requests.get("https://api.apis.guru/v2/list.json")

print (response.json())