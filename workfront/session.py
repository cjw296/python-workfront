import json
import urllib2
from logging import getLogger
from urllib import urlencode
from warnings import warn

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
        return '{0}: {1!r}'.format(self.code, self.data)

    def __repr__(self):
        return '{0}({1!r}, {2!r})'.format(
            self.__class__.__name__, self.data, self.code
        )


def pretty_json(data):
    return json.dumps(data, sort_keys=True, indent=4)


ONDEMAND_TEMPLATE = '{protocol}://{domain}.attask-ondemand.com/attask/api/{api_version}'
SANDBOX_TEMPLATE = "{protocol}://{domain}.attasksandbox.com/attask/api/{api_version}"


class Session(object):

    session_id = None
    user_id = None

    version_registry = {}

    @classmethod
    def register(cls, api_version):
        cls.version_registry[api_version.version] = api_version

    def __init__(self, domain, api_key=None,
                 ssl_context=None, protocol='https',
                 api_version='unsupported', url_template=ONDEMAND_TEMPLATE):
        self.url = url_template.format(
                protocol=protocol, domain=domain, api_version=api_version
        )
        self.api_key = api_key
        self.ssl_context = ssl_context
        self.api = self.version_registry.get(api_version)
        if self.api is None:
            warn('No APIVersion for {}, only basic requests possible'.format(
                api_version
            ))

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
        elif '://' in path:
            raise TypeError('url not for this session: ' + path)
        else:
            url = self.url + path

        logger.info('url:%s params:%s', url, params)

        try:
            response = urllib2.urlopen(
                url,
                urlencode(params),
                context=self.ssl_context
            )
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

        if 'error' in json_response or code != 200:
            error = json_response.get('error', 'Unknown error, check log')
            raise WorkfrontAPIError(error, code)

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
        converted_params = {}
        for name, value in parameters.items():
            converted_params[object_type.convert_name(name)] = value
        if fields:
            converted_params['fields'] = object_type.field_spec(*fields)
        return [object_type(self, **result) for result in
                self.get('/{}/search'.format(object_type.code), converted_params)]

    def load(self, object_type, ids, fields=None):
        if isinstance(ids, basestring):
            return_multiple = False
        else:
            ids = ','.join(ids)
            return_multiple = True
        params = dict(id=ids)
        if fields:
            params['fields'] = object_type.field_spec(*fields)
        result = self.get('/{}'.format(object_type.code), params)
        if isinstance(result, dict):
            result = object_type(self, **result)
        else:
            result = [object_type(self, **result) for result in result]
        if return_multiple and not isinstance(result, list):
            result = [result]
        return result


# wire in api versions
from .versions.unsupported import api
Session.register(api)
from .versions.v40 import api
Session.register(api)

