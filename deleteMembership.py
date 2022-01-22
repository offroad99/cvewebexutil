import requests
import json
import cveLogger
import sys
import argparse

def deleteMembership(ACCESS_TOKEN, membershipId):
    URL = f"https://api.ciscospark.com/v1/memberships/{membershipId}"
    HEADERS = {"Content-type" : "application/json; charset=utf-8", "Authorization" : "Bearer " + ACCESS_TOKEN}
    response = requests.delete(URL, headers=HEADERS)
    cveLogger.mylogger(f'{cveLogger.lineno()} delete response: {response.status_code}')
    if response.status_code in {200, 204}:
        cveLogger.mylogger(f'{cveLogger.lineno()} delete successful')
    else:
        cveLogger.mylogger(f'{cveLogger.lineno()} delete failed')

if __name__ == "__main__":
    cveLogger.initlogging(sys.argv)
    cveLogger.mylogger(f'{cveLogger.lineno()} About to begin deleteMembership')
    ACCESS_TOKEN = input('bearer token: ')
    membershipId = input('Membership ID: ')
    deleteMembership(ACCESS_TOKEN, membershipId)