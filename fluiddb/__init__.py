"""Fluiddb python api"""

import httplib2
import urllib

try:
    import json
except ImportError:
    import simplejson as json

prefix = 'http://fluiddb.fluidinfo.com'

def call(method, path, body=None, **kwargs):
    """call a method in FluidDB http"""
    http = httplib2.Http()
    url = prefix + urllib.quote(path)
    if kwargs:
        url = '%s?%s' % (url, urllib.urlencode(kwargs))
    headers = dict(Accept='application/json')
    if body:
        headers['content-type'] = 'application/json'
    response, result = http.request(url, method, body, headers)
    status = response.status
    if response['content-type'].startswith('application/json'):
        result = json.loads(result)
    return status, result
