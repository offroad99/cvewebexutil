import requests
import json


import requests

URL = "https://api.ciscospark.com/v1/messages"

ACCESS_TOKEN = "ZmZjODY3OTEtODNjZS00Yjg0LTlhN2QtOWVlYWU2ZjgzNWFjYmE1ZmZkMGYtMjg0"

HEADERS = {"Content-type" : "application/json; charset=utf-8", "Authorization" : "Bearer " + ACCESS_TOKEN}
PARAMS = {"roomId" : "Y2lzY29zcGFyazovL3VzL1JPT00vOWUwYTZmOTAtODE2YS0xMWU3LWE0OTItZjViNmJlNGQxZWRk", "max" : "500"}

response = requests.get(url=URL, headers=HEADERS, params=PARAMS)

result = response.json()

print(response.status_code)
#print(response.text)

#print json.dumps(result, indent=4, separators=(',', ': '))

for val in result["items"]:
  print val["personEmail"] + " " + val["personId"] + " " + val["created"]
