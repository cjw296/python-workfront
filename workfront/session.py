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

    def __init__(self, data, code):
        self.data = data
        self.code = code

    def __str__(self):
        return '{0}: {1!r}'.format(self.code, repr(self.data))


def pretty_json(data):
    return json.dumps(data, sort_keys=True, indent=4)


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
        for key, value in params.items():
            if not isinstance(value, (basestring, int, float)):
                params[key] = json.dumps(value)
        params['method'] = method
        if self.api_key:
            params['apiKey'] = self.api_key
        elif self.session_id:
            params['sessionID'] = self.session_id

        if path.startswith(self.url):
            url = path
        else:
            url = self.url + path

        logger.info('url:%s params:%s', url, params)

        try:
            response = urllib2.urlopen(url, urlencode(params), context=self.ssl_context)
            code = response.code
        except urllib2.HTTPError as e:
            response = e
            code = e.code

        text = response.read()
        try:
            json_response = json.loads(text)
        except ValueError as e:
            json_response = dict(error=dict(exception=str(e), response=text))

        logger.debug('returned: %s', pretty_json(json_response))

        if 'error' in json_response:
            raise WorkfrontAPIError(json_response['error'], code)

        return json_response['data']

    def get(self, path, params=None):
        return self.request(GET, path, params)

    def post(self, path, params=None):
        return self.request(POST, path, params)

    def put(self, path, params=None):
        return self.request(PUT, path, params)

    def delete(self, path, params=None):
        return self.request(DELETE, path, params)

    def login(self, username, password):
        data = self.get('/login', dict(username=username, password=password))
        self.session_id = data['sessionID']
        self.user_id = data['userID']

    def logout(self):
        self.get('/logout')
        del self.session_id
        del self.user_id

    def get_api_key(self, username, password):
        params = dict(action='getApiKey', username=username, password=password)
        return self.put('/user', params)['result']

    def search(self, object_type, fields=None, **parameters):
        if fields:
            parameters['fields'] = object_type.field_spec(*fields)
        results = []
        for result in self.get('/{}/search'.format(object_type.code), parameters):
            results.append(object_type(self, **result))
        return results

