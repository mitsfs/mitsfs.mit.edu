#!/usr/bin/python

from flup.server.fcgi import WSGIServer
import requests


def app(environ, start_response):
    proxies = {"http": "monolith.mit.edu", "https": "monolith.mit.edu"}

    url = "http://mitsfs.mit.edu/pinkdex?" + environ['QUERY_STRING']
    r = requests.get(url, proxies=proxies)
    start_response(str(r.status_code) + " " + r.reason, r.headers.items())
    yield str(r.text)

WSGIServer(app).run()
