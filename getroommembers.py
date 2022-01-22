import requests
import json
import sys
import argparse

USAGE = 'python ' + sys.argv[0] + ' <room id>\n\n'

if len(sys.argv) == 1:
  print(USAGE)
  myroomId = input('room id: ')
else:
  myroomId = sys.argv[1]
#print (f'this is the room ID: {myroomId}\n')
savetofile = False
URL = "https://api.ciscospark.com/hydra/api/v1/memberships"
ACCESS_TOKEN = input('bearer token: ')
saveto = input('file name to save to(enter "screen" or leave empty to output to screen): ')
if not (saveto.lower() == "screen" or saveto == ''):
  try:
    fhsaveto = open(saveto,'w')
    savetofile = True
  except:
    print(f'Error opening "{saveto}" for writing')
    exit("unable to open file")
  finally:
    fhsaveto.close()
HEADERS = {"Content-type" : "application/json; charset=utf-8", "Authorization" : "Bearer " + ACCESS_TOKEN}
PARAMS = {"roomId" : myroomId}
myNext = True
response = requests.get(url=URL, headers=HEADERS, params=PARAMS)

while myNext == True:
  result = response.json()

  #print(response.status_code)
  #print(response.text)

  #print json.dumps(result, indent=4, separators=(',', ': '))
  try:
    #retrieve the next link header if it exists
    myLink = response.links["next"]
    #print "myLink value is: " + myLink.get('url')
    #retrieve the url from the next link header
    URL = myLink.get('url')
    response = requests.get(url=URL, headers=HEADERS)
  except KeyError:
    #we will hit this exception if there is no next link header
    myNext = False
  if savetofile:
    fhsaveto = open(saveto,'a+')
    for val in result["items"]:
      fhsaveto.write(val["personDisplayName"] + ", " + val["personEmail"] + "\n")
    fhsaveto.close()
  else:
    for val in result["items"]:
      print (val["personDisplayName"] + ", " + val["personEmail"])

