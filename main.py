from flask import Flask, json, session, request, Response, render_template, stream_with_context
import json, sys, requests, re
import os
import datetime
import cveLogger
import sys
import getUserToken
import listUserMemberships
import random, string

clientId = ''
clientSecret = ''

app = Flask(__name__)
app.secret_key = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(18))



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
            cveLogger.mylogger(f'{cveLogger.lineno()} Access Token: {accessToken}')
            expiresIn = codeInfo[1]
            refreshToken = codeInfo[2]
            redirectUri = codeInfo[3]
            session['accessToken'] = accessToken
            session['expiresIn'] = expiresIn
            session['refreshToken'] = refreshToken
            session['redirectUri'] = redirectUri
            return render_template("removeUser.html.jinja", accessStuff = accessToken)
            
        return "Auth failed. Review logs"

    return render_template("index.html.jinja")

@app.route("/removeUser", methods=["GET"])
def removeUserRender():
    cveLogger.mylogger(f'{cveLogger.lineno()} got here with request view_args: {request.query_string}')
    cveLogger.mylogger(f'{cveLogger.lineno()} got here with request referrer: {request.referrer}')   
    return render_template("removeUser.html.jinja")

@app.route("/removeUserStatus", methods=["POST", "GET"])
def removeUserStatus():

    # Webhook Receiver
    cveLogger.mylogger(f'{cveLogger.lineno()} got here with request: {request.args}')
    
    if request.method == "POST":
        cveLogger.mylogger(f'{cveLogger.lineno()} request method is post')
        cveLogger.mylogger(f'{cveLogger.lineno()} Request content type: {request.content_type}')
        if 'accessToken' in session:
            accessToken = session['accessToken']
            session['emailAddress'] = request.args.get('emailAddress')
        else:
            return index()

        return render_template("removeUserStatus.html.jinja", accessStuff = accessToken)

    cveLogger.mylogger(f'{cveLogger.lineno()} request method is not post') 
    if 'emailAddress' in session:
        return app.response_class(listUserMemberships.listUserMemberships(session['accessToken'], session['emailAddress'], ''), mimetype="text/plain")



if __name__ == "__main__":
    cveLogger.initlogging(sys.argv)
    cveLogger.mylogger(f'{cveLogger.lineno()} About to begin web server on port 5001')
    app.run(host="0.0.0.0", port=443, debug=True, 
        ssl_context=('/etc/letsencrypt/live/cveautomation.com/fullchain.pem', '/etc/letsencrypt/live/cveautomation.com/privkey.pem'))