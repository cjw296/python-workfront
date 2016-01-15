from io import StringIO
from urllib2 import HTTPError


class MockResponse(StringIO):
    def __init__(self, content, code):
        super(MockResponse, self).__init__(unicode(content))
        self.code = code


class MockHTTPError(HTTPError):
    def __init__(self, content, code):
        self.read = StringIO(unicode(content)).read
        self.code = code

class MockOpen(dict):

    def __call__(self, url, params, context):
        response, code = self[url, params, context]
        if isinstance(response, Exception):
            raise response
        return MockResponse(response, code)

    def add(self, url, response, params='', code=200, ssl_context=None):
        self[url, params, ssl_context] = response, code
