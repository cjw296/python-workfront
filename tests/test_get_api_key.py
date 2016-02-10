from unittest import TestCase

from mock import Mock
from testfixtures import Replacer, OutputCapture, ShouldRaise

from tests.helpers import MockOpen
from workfront.get_api_key import main
from workfront.session import WorkfrontAPIError
from workfront.six import PY2


class TestGetApiKey(TestCase):

    def setUp(self):
        r = Replacer()
        self.addCleanup(r.restore)
        self.mock = Mock()
        self.mock.input.return_value = 'u'
        self.mock.getpass.return_value = 'p'
        r.replace('workfront.get_api_key.input', self.mock.input)
        r.replace('getpass.getpass', self.mock.getpass)
        r.replace('logging.basicConfig', self.mock.logging)
        r.replace('sys.argv', ['x'])
        self.server = MockOpen(
            'https://api-cl01.attask-ondemand.com/attask/api/unsupported'
        )
        r.replace('workfront.six.moves.urllib.urlopen',
                  self.server, strict=False)

    def test_functional(self):
        self.server.add(
            url='/user',
            params='action=getApiKey&method=PUT&username=u&password=p',
            response='{"data": {"result": "xyz"}}'
        )
        with OutputCapture() as output:
            main()

        if PY2:
            expected="Your API key is: u'xyz'"
        else:
            expected="Your API key is: 'xyz'"
        output.compare(expected)

    def test_api_error(self):
        self.server.add(
            url='/user',
            params='action=getApiKey&method=PUT&username=u&password=p',
            response='{"error": "your foo went bar"}'
        )
        with ShouldRaise(WorkfrontAPIError(u'your foo went bar', 200)):
            with OutputCapture() as output:
                main()

        output.compare("")

