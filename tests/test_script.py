import logging
import ssl
from unittest import TestCase

from mock import Mock
from testfixtures import Replacer, OutputCapture, compare, ShouldRaise

from workfront import Session
from workfront.script import parser_with_standard_args, script_setup

default_url = 'https://api-cl01.attask-ondemand.com/attask/api/unsupported'


class TestScript(TestCase):

    def run_it(self, args):
        parser = parser_with_standard_args('test', 'test it')
        parser.add_argument('--test', action='store_true')
        self.logging_config = Mock()
        self.output = OutputCapture()
        with Replacer() as r:
            r.replace('logging.basicConfig', self.logging_config)
            r.replace('sys.argv', ('x '+args).split())
            with self.output:
                self.args, self.session = script_setup(parser)

    def test_default(self):
        self.run_it('')
        compare(self.args.test, False)
        self.assertTrue(isinstance(self.session, Session))
        compare(self.session.url, default_url)
        compare(self.session.ssl_context, None)
        self.logging_config.assert_called_once_with(level=logging.WARNING)

    def test_extra_option(self):
        self.run_it('--test')
        compare(self.args.test, True)
        self.assertTrue(isinstance(self.session, Session))
        compare(self.session.url, default_url)
        compare(self.session.ssl_context, None)
        self.logging_config.assert_called_once_with(level=logging.WARNING)

    def test_unsafe_certs(self):
        self.run_it('--unsafe-certs')
        compare(self.args.test, False)
        self.assertTrue(isinstance(self.session, Session))
        compare(self.session.url, default_url)
        self.assertTrue(self.session.ssl_context)
        self.logging_config.assert_called_once_with(level=logging.WARNING)

    def test_full_url(self):
        self.run_it('--url ftp://foo')
        compare(self.args.test, False)
        self.assertTrue(isinstance(self.session, Session))
        compare(self.session.url, 'ftp://foo')
        compare(self.session.ssl_context, None)
        self.logging_config.assert_called_once_with(level=logging.WARNING)

    def test_protocol_domain_version(self):
        self.run_it('--protocol http --domain foo --version bar')
        compare(self.args.test, False)
        self.assertTrue(isinstance(self.session, Session))
        compare(self.session.url,
                'http://foo.attask-ondemand.com/attask/api/bar')
        compare(self.session.ssl_context, None)
        self.logging_config.assert_called_once_with(level=logging.WARNING)

    def test_url_and_others(self):
        with ShouldRaise(SystemExit(2)):
            self.run_it('--url foo --domain bar')
        self.logging_config.assert_not_called()

    def test_log_level(self):
        self.run_it('--log-level 0')
        compare(self.args.test, False)
        self.assertTrue(isinstance(self.session, Session))
        compare(self.session.url, default_url)
        compare(self.session.ssl_context, None)
        self.logging_config.assert_called_once_with(level=0)
