import json
import sys

from workfront.six import string_types
from workfront.six.moves.urllib import request
from workfront.six.moves.urllib.error import HTTPError
from workfront.six.moves.urllib.parse import urlencode
from logging import getLogger
from warnings import warn

PY34 = sys.version_info[0:2] == (3, 4)

GET = 'GET'
POST = 'POST'
PUT = 'PUT'
DELETE = 'DELETE'

logger = getLogger('workfront')

class WorkfrontAPIError(Exception):
    """
    An exception indicating that an error has been returned by Workfront,
    either in the form of the ``error`` key being provided in the JSON
    response, or a non-200 HTTP status code being sent.
    """

    def __init__(self, data, code):
        #: The ``error`` returned in the response from Workfront, decoded from
        #: JSON if possible, a string otherwise.
        self.data = data
        #: The HTTP response code returned by Workfront.
        self.code = code

    def __str__(self):
        return '{0}: {1!r}'.format(self.code, self.data)

    def __repr__(self):
        return '{0}({1!r}, {2!r})'.format(
            self.__class__.__name__, self.data, self.code
        )


def pretty_json(data):
    return json.dumps(data, sort_keys=True, indent=4)

#: The default URL template used when creating a :class:`~workfront.Session`.
ONDEMAND_TEMPLATE = '{protocol}://{domain}.attask-ondemand.com/attask/api/{api_version}'
#: An alternate URL template that can be used when creating a
#: :class:`~workfront.Session` to the Workfront Sandbox.
SANDBOX_TEMPLATE = "{protocol}://{domain}.attasksandbox.com/attask/api/{api_version}"
HEADERS = {"Content-Type":" application/x-www-form-urlencoded;charset=utf-8"}


class Session(object):
    """
    A session for communicating with the Workfront REST API.

    :param domain: Your Workfront domain name.
    :param api_key: An optional API key to pass with requests made using
                    this session.
    :param ssl_context: An optional :class:`~ssl.SSLContext` to use when
                        communicating with Workfront via SSL.
    :param protocol: The protocol to use, defaults to ``https``.
    :param api_version: The version of the Workfront API to use, defaults to
                        ``unsupported``, which is the newest available.
    :param url_template: The template for Workfront URLs into which
                         ``domain``, ``protocol``, and ``api_version`` will
                         be interpolated.

    .. warning::

        ``ssl_context`` will result in exceptions being raised when used
        under Python 3.4, support exists in Python 2.7 and Python 3.5 onwards.
    """

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
        #: The :class:`~workfront.meta.APIVersion` for the ``api_version``
        #: specified.
        self.api_version = api_version
        self.api = self.version_registry.get(api_version)
        if self.api is None:
            warn('No APIVersion for {}, only basic requests possible'.format(
                api_version
            ))

    def request(self, method, path, params=None):
        """
        The lowest level method for making a request to the Workfront REST API.
        You should only need to use this if you need a ``method`` that isn't
        supported below.

        :param method: The HTTP method to use, eg: ``GET``, ``POST``, ``PUT``.
        :param path: The path element of the URL for the request, eg: ``/user``.
        :param params: A :class:`dict` of parameters to include in the request.
        :return: The JSON-decoded `data` element of the response from Workfront.
        """
        url_params = {}
        if params is not None:
           url_params.update(params)
        for key, value in url_params.items():
            if not isinstance(value, (string_types, int, float)):
                url_params[key] = json.dumps(value)
        url_params['method'] = method
        if self.api_key:
            url_params['apiKey'] = self.api_key
        elif self.session_id:
            url_params['sessionID'] = self.session_id

        if path.startswith(self.url):
            url = path
        elif '://' in path:
            raise TypeError('url not for this session: ' + path)
        else:
            url = self.url + path

        logger.info('url: %s params: %s', url, url_params)

        try:
            body = urlencode(url_params).encode('utf-8')
            kw = {}
            if not PY34:
                kw['context'] = context=self.ssl_context
            response = request.urlopen(
                request.Request(url, body, HEADERS),
                **kw
            )
            code = response.code
        except HTTPError as e:
            response = e
            code = e.code

        text = response.read()
        if isinstance(text, bytes):
            text = text.decode('utf-8')

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
        """
        Perform a ``method=GET`` request to the Workfront REST API.

        :param path: The path element of the URL for the request, eg: ``/user``.
        :param params: A :class:`dict` of parameters to include in the request.
        :return: The JSON-decoded `data` element of the response from Workfront.
        """
        return self.request(GET, path, params)

    def post(self, path, params=None):
        """
        Perform a ``method=POST`` request to the Workfront REST API.

        :param path: The path element of the URL for the request, eg: ``/user``.
        :param params: A :class:`dict` of parameters to include in the request.
        :return: The JSON-decoded `data` element of the response from Workfront.
        """
        return self.request(POST, path, params)

    def put(self, path, params=None):
        """
        Perform a ``method=PUT`` request to the Workfront REST API.

        :param path: The path element of the URL for the request, eg: ``/user``.
        :param params: A :class:`dict` of parameters to include in the request.
        :return: The JSON-decoded `data` element of the response from Workfront.
        """
        return self.request(PUT, path, params)

    def delete(self, path, params=None):
        """
        Perform a ``method=DELETE`` request to the Workfront REST API.

        :param path: The path element of the URL for the request, eg: ``/user``.
        :param params: A :class:`dict` of parameters to include in the request.
        :return: The JSON-decoded `data` element of the response from Workfront.
        """
        return self.request(DELETE, path, params)

    def login(self, username, password):
        """
        Start an ID-based session using the supplied username and password.
        The resulting ``sessionID`` will be passed for all subsequence requests
        using this :class:`Session`.

        The session user's UUID will be stored in :class:`Session.user_id`.
        """
        data = self.get('/login', dict(username=username, password=password))
        self.session_id = data['sessionID']
        self.user_id = data['userID']

    def logout(self):
        """
        End the current ID-based session.
        """
        self.get('/logout')
        del self.session_id
        del self.user_id

    def get_api_key(self, username, password):
        """
        Return the API key for the user with the username and password supplied.

        .. warning::

            If the :class:`Session` is created with an ``api_key``, then that
            key may always be returned, no matter what username or password
            are provided.
        """
        params = dict(action='getApiKey', username=username, password=password)
        return self.put('/user', params)['result']

    def search(self, object_type, fields=None, **parameters):
        """
        Search for :class:`~workfront.meta.Object` instances of the specified
        type.

        :param object_type: The type of object to search for. Should be obtained
                            from the :class:`workfront.Session.api`.
        :param fields: Additional fields to :meth:`~workfront.meta.Object.load`
                       on the returned objects.
                       Nested Object field specifications are supported.
        :param parameters: The search parameters. See the
                           `Workfront documentation`__ for full details.
        :return: A list of objects of the ``object_type`` specified.

        __ https://developers.workfront.com/api-docs/#Search
        """
        converted_params = {}
        for name, value in parameters.items():
            converted_params[object_type.convert_name(name)] = value
        if fields:
            converted_params['fields'] = object_type.field_spec(*fields)
        return [
            object_type(self, **result) for result in
            self.get('/{}/search'.format(object_type.code), converted_params)
        ]

    def load(self, object_type, id_or_ids, fields=None):
        """
        Load one or more :class:`~workfront.meta.Object` instances by their
        UUID.
        
        :param object_type: The type of object to search for. Should be obtained
                            from the :class:`workfront.Session.api`.
        :param id_or_ids: A string, when a single object is to be loaded, or a
                          sequence of strings when multiple objects are to be
                          loaded.
        :param fields: The fields to :meth:`~workfront.meta.Object.load`
                       on each object returned. If not specified, the default
                       fields for that object type will be loaded.
        :return: If a single ``id`` is specified, the loaded object will be
                 returned. If ``id_or_ids`` is a sequence, a list of objects
                 will be returned.
        """
        if isinstance(id_or_ids, string_types):
            return_multiple = False
        else:
            id_or_ids = ','.join(id_or_ids)
            return_multiple = True
        params = dict(id=id_or_ids)
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
