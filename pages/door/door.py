#!/usr/bin/python

from cgi import escape
from datetime import datetime, timedelta
import sys, os
from flup.server.fcgi import WSGIServer

logname = "/afs/athena.mit.edu/activity/m/mitsfs/ookcomm/door-sensor/logs/w20-473.log"
states = ["closed", "open"]

def app(environ, start_response):
    last = None
    try:
        error = False
        with open(logname, 'rb') as f:
            f.seek(-64, 2)
            last = f.readlines()[-1].split(",")
            date = datetime.fromtimestamp(int(last[2])).strftime("%R on %A, %F")             
    except ValueError, e:
        raise e

    last = last or [None, 'unknown', None, None]
    state = last[1]
    if last[2]:
        date = datetime.fromtimestamp(int(last[2]))
    else:
        date = 'unknown'

    if (datetime.now() - datetime.fromtimestamp(os.path.getmtime(logname))) > timedelta(minutes = 20):
        state = 'unknown'

    if state not in states:
        error = True

    if error:
        error_code = '500 Internal Server Error'
    else:
        error_code = '200 OK'
    start_response(error_code, [('Content-Type', 'text/html')])
    
    yield '<!DOCTYPE html><html>'
    yield '<head>'
    yield '''
<style>
body {
    font-family: "Helvetica Neue",Helvetica,Arial,sans-serif;
    line-height: 1.2em;
    color: #e7e7e6;
    background-color: #a31f34;
    margin: 0;
    padding: 0;
    overflow: hidden;
    width: 100%;
    height: 100%;
    font-size: 18px;
    font-variant: small-caps;
    vertical-align:middle;
}
p {
    margin-top: 5px;
    padding: 0px;
}
</style>'''
    yield '<title>MIT Science Fiction Library is %s</title>' % (state.title())
    yield '</head>'
    yield '<body><p>Library is %s Right Now</p></body>' % (state.title())
    yield '</html>'

WSGIServer(app).run()
