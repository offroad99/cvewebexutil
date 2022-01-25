from flask import Flask, json, request, Response, render_template, stream_with_context
import json, sys, requests, re
import os
import datetime
import cveLogger
import sys
import getUserToken

clientId = ''
clientSecret = ''

app = Flask(__name__)

@app.route('/')
def index():
    cveLogger.mylogger(f'{cveLogger.lineno()} got here with request view_args: {request.query_string}')
    cveLogger.mylogger(f'{cveLogger.lineno()} got here with request referrer: {request.referrer}')    
    global clientSecret
    global clientId

    code = request.args.get('code')
    state = request.args.get('state')

    if code and state:
        codeInfo = getUserToken.getWebexUserToken(code)
        if codeInfo:
            accessToken = codeInfo[0]
            expiresIn = codeInfo[1]
            refreshToken = codeInfo[2]
            redirectUri = codeInfo[3]
            return "Successfully received auth"
        return "Auth failed. Review logs"

    return "Error in request", 400


@app.route("/", methods=["POST"])
def login_dnac():

    # Webhook Receiver
    cveLogger.mylogger(f'{cveLogger.lineno()} got here with request: {request.json}')
    webhook_data = request.json
    #pprint(webhook_data)
    #webhook_data = json.dumps(webhook_data)


if __name__ == "__main__":
    cveLogger.initlogging(sys.argv)
    cveLogger.mylogger(f'{cveLogger.lineno()} About to begin web server on port 5001')
    app.run(host="0.0.0.0", port=443, debug=True, 
        ssl_context=('/etc/letsencrypt/live/cveautomation.com/fullchain.pem', '/etc/letsencrypt/live/cveautomation.com/privkey.pem'))