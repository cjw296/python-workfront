import re
from doctest import REPORT_NDIFF, ELLIPSIS, OutputChecker
from glob import glob
from manuel import doctest, codeblock
from manuel.testing import TestSuite, os
from nose.plugins.skip import SkipTest
from os.path import dirname, join, pardir
from testfixtures import Replacer

from tests.helpers import MockOpen
from workfront.six import PY3

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
    ],
    use=[
        dict(
            url='https://yourdomain.attask-ondemand.com/attask/api/unsupported/login',
            params='method=GET&username=youruser&password=yourpassword',
            response='{"data": {"sessionID": "xyz123", "userID": "abc456"}}',
        ),
        dict(
            url='https://yourdomain.attask-ondemand.com/attask/api/unsupported/logout',
            params='method=GET&sessionID=xyz123',
            response='{"data": null}',
        ),
        dict(
            url='https://yourdomain.attask-ondemand.com/attask/api/v4.0/PROJ/search',
            params='method=GET&name=project name&name_Mod=cicontains',
            response='{"data": [{"ID": "def789", "name": "The Project Name"}]}',
        ),
        dict(
            url='https://yourdomain.attask-ondemand.com/attask/api/v4.0/TASK/search',
            params='method=GET&projectID=def789&status=CLS&status_Mod=ne&fields=resolvables:*',
            response='{"data": [{"ID": "ghi101", "name": "Something to do", '
                     '"resolvables": [{"ID": "jkl112", "objCode": "OPTASK"}]}]}',
        ),
        # ID is okay, id is okay, but not Id or iD...
        dict(
            url='https://yourdomain.attask-ondemand.com/attask/api/v4.0/PROJ',
            params='method=GET&id=def789',
            response='{"data": {"ID": "def789", "name": "The Project Name"}}',
        ),
        dict(
            url='https://yourdomain.attask-ondemand.com/attask/api/v4.0/PROJ',
            params='method=GET&id=def789',
            response='{"data": [{"ID": "def789", "name": "The Project Name"}]}',
        ),
        dict(
            url='https://yourdomain.attask-ondemand.com/attask/api/v4.0/OPTASK',
            params='method=POST&projectID=def789&name=something bad&description=details',
            response='{"data": {"ID": "klm429"}}',
        ),
        dict(
            url='https://yourdomain.attask-ondemand.com/attask/api/v4.0/OPTASK/klm429',
            params='method=PUT&description=details\nautomatically appended text.',
            response='{"data": {}}',
        ),
        dict(
            url='https://yourdomain.attask-ondemand.com/attask/api/v4.0/OPTASK/klm429',
            params='method=GET&fields=previousStatus',
            response='{"data": {"previousStatus": "CLS"}}',
        ),
        dict(
            url='https://yourdomain.attask-ondemand.com/attask/api/v4.0/OPTASK/klm429',
            params='method=DELETE',
            response='{"data": {}}',
        ),
        dict(
            url='https://yourdomain.attask-ondemand.com/attask/api/v4.0/OPTASK/klm429',
            params='method=GET&fields=project',
            response='{"data": {"project": {"ID": "def789", "name": "The Project Name", "objCode": "PROJ"}}}',
        ),
        dict(
            url='https://yourdomain.attask-ondemand.com/attask/api/v4.0/OPTASK/klm429',
            params='method=PUT&projectID=ghj1234',
            response='{"data": {}}',
        ),
        dict(
            url='https://yourdomain.attask-ondemand.com/attask/api/v4.0/OPTASK/klm429',
            params='method=GET&fields=project',
            response='{"data": {"project": {"ID": "ghj1234", "name": "Another Project", "objCode": "PROJ"}}}',
        ),
        dict(
            url='https://yourdomain.attask-ondemand.com/attask/api/v4.0/OPTASK/klm429',
            params='method=GET&fields=resolvables',
            response='{"data": {"resolvables": [{"ID": "tsk345", "objCode": "TASK"}]}}',
        ),
        dict(
            url='https://yourdomain.attask-ondemand.com/attask/api/v4.0/OPTASK/klm429/markDone',
            params='method=PUT&status=CLS',
            response='{"data": {}}',
        ),
        dict(
            url='https://yourdomain.attask-ondemand.com/attask/api/v4.0/something/New',
            params='method=POST&apiKey=my key&just=in case',
            response='{"data": ["result", 42]}',
        ),
        dict(
            url='https://yourdomain.attask-ondemand.com/attask/api/v4.0/foo',
            params='method=TEST&apiKey=my key&what=now',
            response='{"data": "some data"}',
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


if PY3:
    UNICODE_LITERALS = re.compile("u('.+?')", re.MULTILINE)

    class DocTestChecker(OutputChecker):
        def check_output(self, want, got, optionflags):
            want = UNICODE_LITERALS.sub('\\1', want)
            want = want.replace('FieldNotLoaded: ',
                                'workfront.meta.FieldNotLoaded: ')
            return OutputChecker.check_output(
                self, want, got, optionflags
                )
else:
    DocTestChecker = OutputChecker


def test_suite():
    m = doctest.Manuel(optionflags=REPORT_NDIFF | ELLIPSIS,
                       checker=DocTestChecker())
    m += codeblock.Manuel()
    return TestSuite(m, setUp=set_up, *tests)
