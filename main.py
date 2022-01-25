from flask import Flask, json, request, Response, render_template, stream_with_context
import json, sys, requests, re
import os
import datetime
import cveLogger
import sys


app = Flask(__name__)

@app.route('/')
def index():
    
    cveLogger.mylogger(f'{cveLogger.lineno()} got here with request view_args: {request.query_string}')
    cveLogger.mylogger(f'{cveLogger.lineno()} got here with request data: {request.data}')
    cveLogger.mylogger(f'{cveLogger.lineno()} got here with request view_args: {request.view_args}')
    cveLogger.mylogger(f'{cveLogger.lineno()} got here with request referrer: {request.referrer}')
    return app.response_class("Successfully received request", mimetype="text/plain")


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