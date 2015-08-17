from logging import getLogger
from urllib import urlencode

import json
import urllib2


GET = 'GET'
POST = 'POST'
PUT = 'PUT'
DELETE = 'DELETE'

logger = getLogger('workfront')

class WorkfrontAPIError(Exception):

    def __init__(self, data):
        self.data = data

    def __str__(self):
        return repr(self.data)


class Session(object):

    session_id = None
    user_id = None

    def __init__(self, domain, api_key=None,
                 ssl_context=None, protocol='https', api_version='unsupported',
                 url_template='{protocol}://{domain}.attask-ondemand.com/attask/api/{api_version}'):
        self.url = url_template.format(protocol=protocol, domain=domain, api_version=api_version)
        self.api_key = api_key
        self.ssl_context = ssl_context

    def request(self, method, path, params=None):
        if params is None:
            params = {}
        params['method'] = method
        if self.api_key:
            params['apiKey'] = self.api_key
        elif self.session_id:
            params['sessionID'] = self.session_id

        url = self.url + path
        logger.info('url:%s params:%s', url, params)

        try:
            response = urllib2.urlopen(url, urlencode(params), context=self.ssl_context)
        except urllib2.HTTPError as e:
            response = e
        json_response = json.load(response)

        if 'error' in json_response:
            raise WorkfrontAPIError(json_response['error'])

        return json_response['data']

    def login(self, username, password):
        data = self.request(GET, '/login', dict(username=username, password=password))
        self.session_id = data['sessionID']
        self.user_id = data['userID']

    def logout(self):
        self.request(GET, '/logout')
        del self.session_id
        del self.user_id

    def get_api_key(self, username, password):
        params = dict(action='getApiKey', username=username, password=password)
        return self.request(PUT, '/user', params)['result']

