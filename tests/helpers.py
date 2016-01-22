from io import StringIO
from urllib2 import HTTPError
from urlparse import parse_qs

from testfixtures import compare


class MockResponse(StringIO):
    def __init__(self, content, code):
        super(MockResponse, self).__init__(unicode(content))
        self.code = code


class MockHTTPError(HTTPError):
    def __init__(self, content, code):
        self.read = StringIO(unicode(content)).read
        self.code = code

class MockOpen(dict):

    added = 0
    calls = 0

    def __init__(self, base_url):
        self.base_url = base_url

    def decode(self, params):
        bits = []
        for key, value in parse_qs(params).items():
            if isinstance(value, list):
                value = tuple(value)
            bits.append((key, value))
        return tuple(sorted(bits))

    def __call__(self, url, params, context):
        key = self.calls, url, self.decode(params), context
        try:
            response, code = self[key]
        except KeyError:  # pragma: no cover
            parts = []
            for expected in sorted(self.keys()):
                parts.append(compare(expected, actual=key, raises=False))
            raise AssertionError('\n'.join(parts))

        self.calls += 1
        if isinstance(response, Exception):
            raise response
        return MockResponse(response, code)

    def add(self, url, response, params='', code=200, ssl_context=None):
        self[self.added,
             self.base_url + url,
             self.decode(params),
             ssl_context] = response, code
        self.added += 1

    def assert_called(self, times):
        compare(self.added, expected=times)
