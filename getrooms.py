import requests
import json
import cveLogger
import sys

def getRooms(ACCESS_TOKEN, roomname):
    linkheader = None
    first = True
    URL = "https://api.ciscospark.com/v1/rooms"
    HEADERS = {"Content-type" : "application/json; charset=utf-8", "Authorization" : "Bearer " + ACCESS_TOKEN}
    PARAMS = {"type" : "group", "max" : "100"}
    while first or linkheader is not None:
        first = False
        response = requests.get(url=URL, headers=HEADERS, params=PARAMS)
        #print(response.status_code)
        jsonresp = response.json()
        if response.links.get('next') is not None:
            linkheader = response.links.get('next').get('url')
            if linkheader is not None:
                URL = linkheader
        else:
            linkheader = None
        for room in jsonresp.get('items'):
            if roomname.lower() in room['title'].lower():
                #cveLogger.mylogger(f'{cveLogger.lineno()} Yielding {room["title"]}')
                yield room
                #print(json.dumps(room, indent=4, separators=(',', ': ')))

#print (json.dumps(jsonresp, indent=4, separators=(',', ': ')))
if __name__ == "__main__":
    cveLogger.initlogging(sys.argv)
    cveLogger.mylogger(f'{cveLogger.lineno()} About to begin getRooms')
    ACCESS_TOKEN = input('bearer token: ')
    roomName = input('Room name to searh for: ')
    getRooms(ACCESS_TOKEN, roomName)

    