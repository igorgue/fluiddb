"""Fluiddb python api"""

import httplib2
import urllib

try:
    import json
except ImportError:
    import simplejson as json

prefix = 'http://fluiddb.fluidinfo.com'

global_headers = {
    'Accept': 'application/json',
}

def login(username, password):
    """login by adding auth to the headers"""
    userpass = '%s:%s' % (username, password)
    auth = 'Basic %s' % userpass.encode('base64').strip()
    global_headers['Authorization'] = auth

def logout():
    """logout by deleting the auth header"""
    global_headers.pop('Authorization', None)

def call(method, path, body=None, **kwargs):
    """call a method in FluidDB http"""
    http = httplib2.Http()
    url = prefix + urllib.quote(path)
    if kwargs:
        url = '%s?%s' % (url, urllib.urlencode(kwargs))
    headers = global_headers.copy()
    if isinstance(body, dict):
        headers['content-type'] = 'application/json'
        body = json.dumps(body)
    elif body:
        headers['content-type'] = 'text/plain'
    response, result = http.request(url, method, body, headers)
    status = response.status
    if response['content-type'].startswith('application/json'):
        result = json.loads(result)
    return status, result
