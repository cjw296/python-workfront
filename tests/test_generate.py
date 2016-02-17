import json
from textwrap import dedent
from unittest import TestCase

from mock import Mock
from testfixtures import (
    TempDirectory, Replacer, compare, LogCapture, OutputCapture
)

from tests.helpers import MockOpenHelper
from workfront import Session
from workfront.generate import (
    prepare_target, decorated_object_types, ClassWriter,
    main
)

from workfront.six import StringIO


class TestPrepareTarget(TestCase):

    def setUp(self):
        self.dir = TempDirectory()
        self.addCleanup(self.dir.cleanup)
        replace = Replacer()
        replace('workfront.generate.TARGET_ROOT', self.dir.path)
        self.addCleanup(replace.restore)
        self.session = Session('test')

    def test_from_scratch(self):
        path = prepare_target(self.session)

        compare(path, expected=self.dir.getpath('unsupported.py'))
        self.dir.compare(expected=[])

    def test_everything(self):
        self.dir.write('unsupported.py', b'yy')
        path = prepare_target(self.session)

        compare(path, expected=self.dir.getpath('unsupported.py'))
        self.dir.compare(expected=['unsupported.py'])
        compare(self.dir.read('unsupported.py'), b"yy")

    def test_dots_in_version(self):
        path = prepare_target(Session('test', api_version='v4.0'))

        compare(path, expected=self.dir.getpath('v40.py'))
        self.dir.compare(expected=[])


class TestDecoratedObjectTypes(MockOpenHelper, TestCase):

    def setUp(self):
        super(TestDecoratedObjectTypes, self).setUp()
        self.dir = TempDirectory()
        self.addCleanup(self.dir.cleanup)

    def test_normal(self):
        base_url = 'https://test.attask-ondemand.com/attask/api/v4.0'
        session = Session('test', api_version='v4.0')
        self.server.add(
            url=base_url+'/metadata',
            params='method=GET',
            response=json.dumps(dict(data=dict(objects=dict(
                SomeThing=dict(objCode='SMTHING', name='SomeThing')
            ))))
        )
        expected = dict(
            objCode='SMTHING',
            name='SomeThing',
            stuff='a value'
        )
        self.server.add(
            url=base_url+'/smthing/metadata',
            params='method=GET',
            response=json.dumps(dict(data=expected))
        )
        compare(decorated_object_types(session, None),
                expected=[('SomeThing', 'SMTHING', expected)])

    def test_cache_write(self):
        base_url = 'https://test.attask-ondemand.com/attask/api/v4.0'
        session = Session('test', api_version='v4.0')
        self.server.add(
            url=base_url+'/metadata',
            params='method=GET',
            response=json.dumps(dict(data=dict(objects=dict(
                SomeThing=dict(objCode='SMTHING', name='SomeThing')
            ))))
        )
        expected = dict(
            objCode='SMTHING',
            name='SomeThing',
            stuff='a value'
        )
        self.server.add(
            url=base_url+'/smthing/metadata',
            params='method=GET',
            response=json.dumps(dict(data=expected))
        )
        compare(decorated_object_types(session, self.dir.path),
                expected=[('SomeThing', 'SMTHING', expected)])
        self.dir.compare(expected=[
            'v4.0_metadata.json', 'v4.0_smthing_metadata.json'
        ])
        compare(
            json.loads(self.dir.read('v4.0_metadata.json').decode('ascii')),
            expected=dict(objects=dict(
                SomeThing=dict(objCode='SMTHING', name='SomeThing')
            )))
        compare(
            json.loads(
                self.dir.read('v4.0_smthing_metadata.json').decode('ascii')
            ),
            expected=expected
        )

    def test_cache_read(self):
        expected = dict(
            objCode='SMTHING',
            name='SomeThing',
            stuff='a value'
        )

        self.dir.write('v4.0_metadata.json', json.dumps(dict(objects=dict(
                SomeThing=dict(objCode='SMTHING', name='SomeThing')
        ))), encoding='ascii')

        self.dir.write('v4.0_smthing_metadata.json',
                       json.dumps(expected),
                       encoding='ascii')

        session = Session('test', api_version='v4.0')
        compare(decorated_object_types(session, self.dir.path),
                expected=[('SomeThing', 'SMTHING', expected)])

    def test_unsupported(self):
        base_url = 'https://test.attask-ondemand.com/attask/api/unsupported'
        session = Session('test')
        self.server.add(
            url=base_url+'/metadata',
            params='method=GET',
            response=json.dumps(dict(data=dict(objects=dict(
                SomeThing=dict(objCode='SMTHING', name='SomeThing')
            ))))
        )
        expected = dict(
            objCode='SMTHING',
            name='SomeThing',
            stuff='a value'
        )
        self.server.add(
            url=base_url+'/smthing/metadata',
            params='method=GET',
            response=json.dumps(dict(data=expected))
        )
        compare(decorated_object_types(session, None),
                expected=[('SomeThing', 'SMTHING', expected)])

    def test_name_override(self):
        base_url = 'https://test.attask-ondemand.com/attask/api/unsupported'
        session = Session('test')
        self.server.add(
            url=base_url+'/metadata',
            params='method=GET',
            response=json.dumps(dict(data=dict(objects=dict(
                SomeThing=dict(objCode='OPTASK', name='SomeThing')
            ))))
        )
        expected = dict(
            objCode='SMTHING',
            name='SomeThing',
            stuff='a value'
        )
        self.server.add(
            url=base_url+'/optask/metadata',
            params='method=GET',
            response=json.dumps(dict(data=expected))
        )
        compare(decorated_object_types(session, None),
                expected=[('Issue', 'OPTASK', expected)])


class TestClassWriter(TestCase):

    def setUp(self):
        self.output = StringIO()
        self.writer = ClassWriter('FooBar', 'FOOB', self.output)
        self.log = LogCapture()
        self.addCleanup(self.log.uninstall)

    def check_output(self, expected):
        compare(expected=dedent(expected), actual=self.output.getvalue())

    def test_write_header(self):
        self.writer.write_header()
        self.check_output("""

        class FooBar(Object):
            code = 'FOOB'
        """)

    def test_write_members(self):
        self.output.write('class TestClass(Object):\n')
        self.writer.write_members('Field', ['fooBar', 'BazBob'])
        self.check_output("""\
        class TestClass(Object):
            baz_bob = Field('BazBob')
            foo_bar = Field('fooBar')
        """)

    def test_write_duplicate_members(self):
        self.output.write('class TestClass(Object):\n')
        self.writer.write_members('Field', ['fooBar', 'FooBAR'])
        self.check_output("""\
        class TestClass(Object):
            foo_bar = Field('FooBAR')
            foo_bar = Field('fooBar')
        """)
        self.log.check(
            ('workfront.generate', 'ERROR',
             "FooBar (FOOB) has duplicate member name: "
             "'foo_bar', first from 'FooBAR', current from 'fooBar'")
        )

    def test_member_name_override(self):
        self.output.write('class Approval(Object):\n')
        writer = ClassWriter('Approval', 'TEST', self.output)
        writer.write_members('Field', ['URL', 'url'])
        self.check_output("""\
        class Approval(Object):
            url = Field('URL')
            url_ = Field('url')
        """)
        # no error log:
        self.log.check()

    def test_write_footer(self):
        self.output.write('class FooBar(Object):\n    foo = "bar"\n')
        self.writer.write_footer()
        self.check_output("""\
        class FooBar(Object):
            foo = "bar"

        api.register(FooBar)
        """)


class FunctionalTest(MockOpenHelper, TestCase):

    base = 'https://api-cl01.attask-ondemand.com/attask/api/unsupported'

    def setUp(self):
        super(FunctionalTest, self).setUp()
        self.log = LogCapture()
        self.addCleanup(self.log.uninstall)
        self.dir = TempDirectory()
        self.addCleanup(self.dir.cleanup)
        self.replace('logging.basicConfig', Mock())
        self.replace('workfront.generate.TARGET_ROOT', self.dir.path)

    def test_functional(self):
        self.replace('sys.argv', ['x'])

        self.server.add(
            url='/metadata',
            params='method=GET',
            response=json.dumps(dict(data=dict(objects=dict(
                SomeThing=dict(objCode='BAR', name='SomeThing'),
                OtherThing=dict(objCode='FOO', name='OtherThing'),
            ))))
        )

        self.server.add(
            url='/foo/metadata',
            params='method=GET',
            response=json.dumps(dict(data=dict(
                objCode='FOO',
                name='OtherThing',
                fields={"ID": {}, "anotherField": {}},
                references={},
                collections={},
            )))
        )

        self.server.add(
            url='/bar/metadata',
            params='method=GET',
            response=json.dumps(dict(data=dict(
                objCode='BAR',
                name='SomeThing',
                fields={"ID": {}, "theField": {}},
                references={"accessRules": {}},
                collections={"assignedTo": {}},
            )))
        )

        with OutputCapture() as output:
            output.disable()
            main()

        output.compare("")

        self.dir.compare(expected=['unsupported.py'])

        compare(self.dir.read('unsupported.py'), expected=b"""\
# generated from https://api-cl01.attask-ondemand.com/attask/api/unsupported/metadata
from ..meta import APIVersion, Object, Field, Reference, Collection

api = APIVersion('unsupported')


class OtherThing(Object):
    code = 'FOO'
    another_field = Field('anotherField')

api.register(OtherThing)


class SomeThing(Object):
    code = 'BAR'
    the_field = Field('theField')
    access_rules = Reference('accessRules')
    assigned_to = Collection('assignedTo')

api.register(SomeThing)
""")
