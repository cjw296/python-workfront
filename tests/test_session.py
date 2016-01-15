from unittest import TestCase
from urllib2 import HTTPError

from testfixtures import Replacer, compare, ShouldRaise

from tests.helpers import MockOpen, MockHTTPError
from workfront import Session
from workfront.session import SANDBOX_TEMPLATE, WorkfrontAPIError


class SessionTests(TestCase):

    def setUp(self):
        r = Replacer()
        self.addCleanup(r.restore)
        self.server = MockOpen()
        r.replace('urllib2.urlopen', self.server)

    def test_basic_request(self):
        session = Session('test')
        self.server.add(
            url='https://test.attask-ondemand.com/attask/api/unsupported/login',
            params='method=GET',
            response='{"data": "foo"}'
        )
        compare(session.get('/login'), expected='foo')

    def test_different_protocol_and_version(self):
        session = Session('test', protocol='http', api_version='v4.0')
        self.server.add(
            url='http://test.attask-ondemand.com/attask/api/v4.0/login',
            params='method=GET',
            response='{"data": "foo"}'
        )
        compare(session.get('/login'), expected='foo')

    def test_different_url_template(self):
        session = Session('test', url_template=SANDBOX_TEMPLATE)
        self.server.add(
            url='https://test.attasksandbox.com/attask/api/unsupported/login',
            params='method=GET',
            response='{"data": "foo"}'
        )
        compare(session.get('/login'), expected='foo')
