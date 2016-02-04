import json
from unittest import TestCase

from testfixtures import TempDirectory, Replacer, compare

from tests.helpers import MockOpenHelper
from workfront import Session
from workfront.generate import prepare_target, INIT_TEMPLATE, \
    decorated_object_types


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

        compare(path, expected=self.dir.getpath('unsupported/generated.py'))
        self.dir.compare([
            'unsupported/',
            'unsupported/__init__.py',
        ])

        compare(self.dir.read('unsupported/__init__.py'), INIT_TEMPLATE)

    def test_just_dir(self):
        self.dir.makedir('unsupported')
        path = prepare_target(self.session)

        compare(path, expected=self.dir.getpath('unsupported/generated.py'))
        self.dir.compare([
            'unsupported/',
            'unsupported/__init__.py',
        ])

        compare(self.dir.read('unsupported/__init__.py'), INIT_TEMPLATE)

    def test_dir_and_init(self):
        self.dir.write('unsupported/__init__.py', 'xx')
        path = prepare_target(self.session)

        compare(path, expected=self.dir.getpath('unsupported/generated.py'))
        self.dir.compare([
            'unsupported/',
            'unsupported/__init__.py',
        ])

        compare(self.dir.read('unsupported/__init__.py'), "xx")

    def test_everything(self):
        self.dir.write('unsupported/__init__.py', 'xx')
        self.dir.write('unsupported/generated.py', 'yy')
        path = prepare_target(self.session)

        compare(path, expected=self.dir.getpath('unsupported/generated.py'))
        self.dir.compare([
            'unsupported/',
            'unsupported/__init__.py',
            'unsupported/generated.py',
        ])

        compare(self.dir.read('unsupported/__init__.py'), "xx")
        compare(self.dir.read('unsupported/generated.py'), "yy")


class TestDecoratedObjectTypes(MockOpenHelper, TestCase):

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
        compare(decorated_object_types(session),
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
        compare(decorated_object_types(session),
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
        compare(decorated_object_types(session),
                expected=[('Issue', 'OPTASK', expected)])
