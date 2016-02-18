import json
from io import StringIO
from workfront.six import text_type, string_types
from workfront.six.moves.urllib.error import HTTPError
from workfront.six.moves.urllib.parse import parse_qs
from workfront.session import  PY34

from testfixtures import compare, Replacer

from workfront import Session
from workfront.meta import APIVersion, Object, Field


class MockResponse(StringIO):
    def __init__(self, content, code):
        super(MockResponse, self).__init__(text_type(content))
        self.code = code


class MockHTTPError(HTTPError):
    def __init__(self, content, code):
        self.read = StringIO(text_type(content)).read
        self.code = code


class MockOpen(dict):

    added = 0
    calls = 0

    def __init__(self, base_url):
        self.base_url = base_url

    def decode(self, params):
        if isinstance(params, bytes):
            params = params.decode('utf-8')
        bits = []
        for key, value in parse_qs(params).items():
            if isinstance(value, list):
                if len(value) == 1:
                    value = value[0]
                else: # pragma: no cover
                    value = tuple(value)
            if isinstance(value, string_types) and value[0] == '{':
                value = json.dumps(json.loads(value), sort_keys=True)
            bits.append((key, value))
        return tuple(sorted(bits))

    def __call__(self, request, context=None):
        params = self.decode(request.data)
        url = request.get_full_url()
        key = self.calls, url, params, context
        try:
            response, code = self[key]
        except KeyError:  # pragma: no cover
            parts = []
            for expected in sorted(self.keys()):
                parts.append(compare(expected, actual=key, raises=False))
            if parts:
                raise AssertionError('\n'.join(parts))
            else:
                raise KeyError(key)

        self.calls += 1
        if isinstance(response, Exception):
            raise response
        return MockResponse(response, code)

    def add(self, url, response, params='', code=200, ssl_context=None):
        # Python 3.4 doesn't support ssl contexts, so just ignore them:
        if PY34:
            ssl_context = None

        if not url.startswith('http'):
            url = self.base_url + url
        self[self.added,
             url,
             self.decode(params),
             ssl_context] = response, code
        self.added += 1

    def assert_called(self, times):
        compare(self.added, expected=times)


class MockOpenHelper(object):

    base = 'https://test.attask-ondemand.com/attask/api/unsupported'

    def setUp(self):
        self.replace = Replacer()
        self.addCleanup(self.replace.restore)
        self.server = MockOpen(self.base)
        self.replace('workfront.six.moves.urllib.request.urlopen', self.server)


class TestObjectHelper(MockOpenHelper):

    base = 'https://test.attask-ondemand.com/attask/api/test'

    def setUp(self):
        super(TestObjectHelper, self).setUp()
        self.replace('workfront.session.Session.version_registry', {})
        test_api = APIVersion('test')
        class TestObject(Object):
            code='TEST'
            field_one = Field('fieldOne')
            field_two = Field('fieldTwo')
        test_api.register(TestObject)
        Session.register(test_api)
        self.session = Session('test', api_version='test')
        self.api = self.session.api
