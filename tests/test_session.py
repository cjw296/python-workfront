import ssl
from unittest import TestCase

from testfixtures import compare, ShouldRaise, ShouldWarn

from tests.helpers import MockHTTPError, MockOpenHelper
from workfront import Session
from workfront.session import SANDBOX_TEMPLATE, WorkfrontAPIError


class SessionTests(MockOpenHelper, TestCase):

    def test_basic_request(self):
        session = Session('test')
        self.server.add(
            url='/login',
            params='method=GET',
            response='{"data": "foo"}'
        )
        compare(session.get('/login'), expected='foo')
        self.server.assert_called(times=1)

    def test_different_protocol_and_version(self):
        self.server.base_url = ''
        session = Session('test', protocol='http', api_version='v4.0')
        self.server.add(
            url='http://test.attask-ondemand.com/attask/api/v4.0/login',
            params='method=GET',
            response='{"data": "foo"}'
        )
        compare(session.get('/login'), expected='foo')
        self.server.assert_called(times=1)

    def test_different_url_template(self):
        self.server.base_url = ''
        session = Session('test', url_template=SANDBOX_TEMPLATE)
        self.server.add(
            url='https://test.attasksandbox.com/attask/api/unsupported/login',
            params='method=GET',
            response='{"data": "foo"}'
        )
        compare(session.get('/login'), expected='foo')
        self.server.assert_called(times=1)

    def test_http_error(self):
        # somewhat hypothetical, error is usually in the return json
        session = Session('test')
        self.server.add(
            url='/login',
            params='method=GET',
            response=MockHTTPError('{"data": "foo"}', 500),
        )
        with ShouldRaise(WorkfrontAPIError('Unknown error, check log', 500)):
            session.get('/login')
        self.server.assert_called(times=1)

    def test_api_error(self):
        session = Session('test')
        self.server.add(
            url='/',
            params='method=GET',
            response='{"error":{'
                     '"class":"java.lang.UnsupportedOperationException",'
                     '"message":"you must specify an action"}}'
        )
        with ShouldRaise(WorkfrontAPIError(
                {u'message': u'you must specify an action',
                 u'class': u'java.lang.UnsupportedOperationException'},
                200
        )):
            session.get('/')
        self.server.assert_called(times=1)

    def test_api_error_str_and_repr(self):
        error = WorkfrontAPIError('data', 503)
        compare(str(error), expected="503: 'data'")
        compare(repr(error), expected="WorkfrontAPIError('data', 503)")

    def test_other_error(self):
        session = Session('test')
        self.server.add(
            url='/',
            params='method=GET',
            response=Exception('boom!')
        )
        with ShouldRaise(Exception('boom!')):
            session.get('/')
        self.server.assert_called(times=1)

    def test_bad_json(self):
        session = Session('test')
        self.server.add(
            url='/',
            params='method=GET',
            response="{'oops': 'not json'}"
        )
        with ShouldRaise(WorkfrontAPIError(
                {'exception': 'Expecting property name enclosed in double '
                              'quotes: line 1 column 2 (char 1)',
                 'response': u"{'oops': 'not json'}"},
                200
        )):
            session.get('/')
        self.server.assert_called(times=1)

    def test_insecure_context(self):
        context = ssl._create_unverified_context()
        session = Session('test', ssl_context=context)
        self.server.add(
            url='/login',
            params='method=GET',
            response='{"data": "foo"}',
            ssl_context=context
        )
        compare(session.get('/login'), expected='foo')
        self.server.assert_called(times=1)

    def test_login(self):
        session = Session('test')
        self.server.add(
            url='/login',
            params='method=GET&username=u&password=p',
            response='{"data": {"sessionID": "x", "userID": "uid"}}'
        )
        session.login('u', 'p')
        compare(session.session_id, 'x')
        compare(session.user_id, 'uid')
        self.server.assert_called(times=1)
        return session

    def test_logout(self):
        session = self.test_login()
        self.server.add(
            url='/logout',
            params='method=GET&sessionID=x',
            response='{"data": null}'
        )
        session.logout()
        compare(session.session_id, None)
        compare(session.user_id, None)
        self.server.assert_called(times=2)

    def test_request_with_session_id(self):
        session = self.test_login()
        self.server.add(
            url='/ISSUE',
            params='method=GET&sessionID=x',
            response='{"data": "foo"}'
        )
        compare(session.get('/ISSUE'), 'foo')
        self.server.assert_called(times=2)

    def test_get_api_key(self):
        session = Session('test')
        self.server.add(
            url='/user',
            params='method=PUT&action=getApiKey&username=u&password=p',
            response='{"data": {"result": "xyz"}}'
        )
        compare(session.get_api_key('u', 'p'), 'xyz')
        self.server.assert_called(times=1)

    def test_request_with_api_key(self):
        session = Session('test', api_key='xyz')
        self.server.add(
            url='/ISSUE',
            params='method=GET&apiKey=xyz',
            response='{"data": "foo"}'
        )
        actual = session.request('GET', '/ISSUE')
        compare(actual, expected='foo')
        self.server.assert_called(times=1)

    def test_request_with_params(self):
        session = Session('test')
        self.server.add(
            url='/endpoint',
            params='method=GET&str=svalue&unicode=uvalue&int=1&float=1.0&'
                   'dict={"key": "value"}',
            response='{"data": "foo"}'
        )
        actual = session.request('GET', '/endpoint', params={
            'str': 'svalue',
            'unicode': u'uvalue',
            'int': 1,
            'float': 1.0,
            'dict': {'key': 'value'},
        })
        compare(actual, expected='foo')
        self.server.assert_called(times=1)

    def test_request_absolute_url(self):

        session = Session('test')
        self.server.add(
            url='/some/url',
            params='method=GET',
            response='{"data": "foo"}'
        )
        actual = session.request(
            'GET',
            'https://test.attask-ondemand.com/attask/api/unsupported/some/url'
        )
        compare(actual, expected='foo')
        self.server.assert_called(times=1)

    def test_request_with_dodgy_absolute_url(self):

        session = Session('test')
        with ShouldRaise(TypeError(
            'url not for this session: '
            'https://bad.example.com/attask/api/unsupported/some/url'
        )):
            session.request(
                'GET',
                'https://bad.example.com/attask/api/unsupported/some/url'
            )

    def test_get(self):
        session = self.test_login()
        self.server.add(
            url='/ISSUE',
            params='sessionID=x&method=GET',
            response='{"data": "foo"}'
        )
        actual = session.get('/ISSUE')
        compare(actual, expected='foo')
        self.server.assert_called(times=2)

    def test_post(self):
        session = self.test_login()
        self.server.add(
            url='/ISSUE',
            params='sessionID=x&method=POST',
            response='{"data": "foo"}'
        )
        actual = session.post('/ISSUE')
        compare(actual, expected='foo')
        self.server.assert_called(times=2)

    def test_put(self):
        session = Session('test', api_key='xyz')
        self.server.add(
            url='/ISSUE',
            params='method=PUT&apiKey=xyz',
            response='{"data": "foo"}'
        )
        actual = session.put('/ISSUE')
        compare(actual, expected='foo')
        self.server.assert_called(times=1)

    def test_delete(self):
        session = Session('test', api_key='xyz')
        self.server.add(
            url='/ISSUE',
            params='method=DELETE&apiKey=xyz',
            response='{"data": "foo"}'
        )
        actual = session.delete('/ISSUE')
        compare(actual, expected='foo')
        self.server.assert_called(times=1)

    def test_warn_on_unknown_api(self):
        with ShouldWarn(UserWarning(
            'No APIVersion for silly, only basic requests possible'
        )):
            Session('test', api_version='silly')

