import requests
import json
import cveLogger
import sys
import argparse

def getRoomMember(ACCESS_TOKEN, roomId, email = None, name = None):
    linkheader = None
    first = True
    URL = "https://api.ciscospark.com/v1/memberships"
    HEADERS = {"Content-type" : "application/json; charset=utf-8", "Authorization" : "Bearer " + ACCESS_TOKEN}
    PARAMS = {
                "roomId" : roomId,
                "personEmail" : email
            }

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
        for person in jsonresp.get('items'):
            if email.lower() in person.get('personEmail').lower():
                cveLogger.mylogger(f'{cveLogger.lineno()} Found person: {person.get("personDisplayName")}')
                cveLogger.mylogger(f'{cveLogger.lineno()} {person}')
                return person
        return None


if __name__ == "__main__":
    cveLogger.initlogging(sys.argv)
    cveLogger.mylogger(f'{cveLogger.lineno()} About to begin getMemberId')
    ACCESS_TOKEN = input('bearer token: ')
    roomId = input('Room ID: ')
    emailAddress = input('Email Address of Person to Find: ')
    getRoomMember(ACCESS_TOKEN, roomId, emailAddress)