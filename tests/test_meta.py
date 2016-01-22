from unittest import TestCase

from testfixtures import compare

from workfront.meta import APIVersion, Object


class TestAPIVersion(TestCase):

    def test_version_string(self):
        api = APIVersion('foo')
        compare(api.version, expected='foo')

    def test_from_data(self):
        api = APIVersion('foo')

        class TestObject(Object):
            code = 'TEST'

        api.register(TestObject)

        session = object()
        result = api.from_data(session, dict(x=1, objCode='TEST'))

        compare(result.session, session)
        compare(result.fields['x'], 1)

    def test_by_name(self):
        api = APIVersion('foo')

        class TestObject(Object):
            code = 'TEST'

        api.register(TestObject)

        result = api.by_name['TestObject']

        compare(result, expected=TestObject)

    def test_override(self):
        api = APIVersion('foo')

        class TestObject(Object):
            code = 'TEST'
        api.register(TestObject)

        class TestObject_(TestObject):
            something = 'foo'
        api.override(TestObject, TestObject_)

        result = api.by_name['TestObject']
        compare(result, expected=TestObject_)
        result = api.from_data(None, dict(objCode='TEST'))
        self.assertTrue(isinstance(result, TestObject_))
        compare(result.something, expected='foo')
