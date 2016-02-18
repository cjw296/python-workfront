from doctest import REPORT_NDIFF, ELLIPSIS
from glob import glob
from manuel import doctest, codeblock
from manuel.testing import TestSuite, os
from nose.plugins.skip import SkipTest
from os.path import dirname, join, pardir
from testfixtures import Replacer

from tests.helpers import MockOpen

tests = glob(join(join(dirname(__file__), pardir), 'docs', '*.rst'))

if not tests:
    # tox can't find docs and installing an sdist doesn't install the docs
    raise SkipTest('No docs found to test')  # pragma: no cover


RESPONSES = dict(
    index=[
        dict(
            url='https://your domain.attask-ondemand.com/attask/api/unsupported/PROJ/search',
            params='method=GET&apiKey=...&name=my project name&name_Mod=cicontains',
            response='{"data": [{"ID": "xxx"}]}',
        ),
        dict(
            url='https://your domain.attask-ondemand.com/attask/api/unsupported/OPTASK',
            params='method=POST&apiKey=...&description=some text here&name=a test issue&projectID=xxx',
            response='{"data": {"ID": "yyy"}}',
        ),
        dict(
            url='https://your domain.attask-ondemand.com/attask/api/unsupported/NOTE',
            params='method=POST&apiKey=...&noteObjCode=OPTASK&noteText=a comment&objID=yyy',
            response='{"data": {"ID": "zzz"}}',
        ),
    ]
)


def set_up(test):
    test.replace = Replacer()
    test.addCleanup(test.replace.restore)
    test.server = MockOpen(
        'https://test.attask-ondemand.com/attask/api/unsupported'
    )
    test.replace('workfront.six.moves.urllib.request.urlopen', test.server)

    filename = os.path.split(str(test))[-1]
    key = os.path.splitext(filename)[0]
    for response in RESPONSES.get(key, ()):
        test.server.add(**response)


def test_suite():
    m = doctest.Manuel(optionflags=REPORT_NDIFF | ELLIPSIS)
    m += codeblock.Manuel()
    return TestSuite(m, setUp=set_up, *tests)
