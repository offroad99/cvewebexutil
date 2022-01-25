import requests
import json
import cveLogger
import sys
import login

def getWebexUserToken(code):
    PARAMS = {
                "grant_type" : "authorization_code", 
                "client_id" : clientId,
                "client_secret" : clientSecret,
                "code" : code,
                "redirect_uri" : "oauth.cveautomation.com"
            }
    
    URL = f'https://webexapis.com/v1/access_token'
    HEADERS = {
            'content-type': "application/x-www-form-urlencoded",
        }
    cveLogger.mylogger(f'{cveLogger.lineno()} About to create global pool with payload: {PAYLOAD}')
    response = requests.post(url=URL, headers=HEADERS, verify=False, params=PARAMS)
    cveLogger.mylogger(f'{cveLogger.lineno()} response.text: {response.text}')
    if response.ok:
        jresponse = response.json()
        return jresponse.get('access_token'), jresponse.get('expires_in'), jresponse.get('refresh_toekn'), jresponse.get('refresh_token_expires_in')
    
    return None