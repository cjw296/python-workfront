from unittest import TestCase

from testfixtures import compare, ShouldRaise

from tests.test_session import MockOpenHelper
from workfront.meta import APIVersion, Object, Field, FieldNotLoaded


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


class TestBaseObject(MockOpenHelper, TestCase):

    def test_field_names(self):
        class TestObject(Object):
            field_one = Field('fieldOne')
            field_two = Field('fieldTwo')
        compare(TestObject.field_names, expected={'field_one', 'field_two'})

    def test_field_names_of_subclass(self):
        class TestObject(Object):
            field_one = Field('fieldOne')
        class TestObject_(TestObject):
            field_two = Field('fieldTwo')
        compare(TestObject_.field_names, expected={'field_one', 'field_two'})

    def test_field_names_of_base_class(self):
        compare(Object.field_names, expected=set())

    def test_instantiate(self):
        class TestObject(Object):
            field_one = Field('fieldOne')
            field_two = Field('fieldTwo')
        session = object()
        obj = TestObject(session, field_one='foo', fieldTwo='bar', ID='x')
        compare(obj.session, session)
        compare(obj.id, 'x')
        compare(obj.field_one, 'foo')
        compare(obj.field_two, 'bar')
        compare(obj.fields.dirty(), {})
        return obj

    def test_instantiate_empty(self):
        class TestObject(Object):
            field_one = Field('fieldOne')
        obj = TestObject()
        compare(obj.session, None)
        compare(obj.id, None)
        with ShouldRaise(FieldNotLoaded('fieldOne')) as s:
            obj.field_one
        self.assertFalse(isinstance(s.raised, AttributeError))
        with ShouldRaise(AttributeError):
            obj.field_two
        compare(obj.fields.dirty(), {})

    def test_repr(self):
        obj = self.test_instantiate()
        compare(
            repr(obj),
            expected="<TestObject: "
                     "{'fieldOne': 'foo', 'fieldTwo': 'bar', 'ID': 'x'}>"
        )

    def test_set_field(self):
        obj = self.test_instantiate()
        obj.field_one = 'boop'
        compare(obj.fields,
                expected={'fieldOne': 'boop', 'fieldTwo': 'bar', 'ID': 'x'})
        compare(obj.fields.dirty(), expected={'fieldOne': 'boop'})

    def test_set_id(self):
        obj = self.test_instantiate()
        with ShouldRaise(AttributeError):
            obj.id = 'nope'

    def test_field_from_class(self):
        obj = self.test_instantiate()
        class_ = obj.__class__
        field = class_.field_one
        self.assertTrue(isinstance(field, Field))
        compare(field.workfront_name, expected='fieldOne')

    def test_convert_name_field_instance(self):
        class TestObject(Object):
            field_one = Field('fieldOne')

        compare(TestObject.convert_name(TestObject.field_one),
                expected='fieldOne')

    def test_convert_name_field_name(self):
        class TestObject(Object):
            field_one = Field('fieldOne')

        compare(TestObject.convert_name('field_one'),
                expected='fieldOne')

    def test_convert_name_fallback(self):
        class TestObject(Object): pass

        compare(TestObject.convert_name('foo'),
                expected='foo')

    def test_field_spec(self):
        class TestObject(Object):
            field_one = Field('fieldOne')

        compare(TestObject.field_spec('field_one', 'fieldTwo'),
                expected='fieldOne,fieldTwo')

    def test_api_url(self):
        class TestObject(Object):
            code = 'FOO'
        compare(TestObject(ID='x').api_url(), expected='/FOO/x')

    def test_api_url_no_id(self):
        class TestObject(Object):
            code = 'FOO'
        with ShouldRaise(ValueError('TestObject has no ID')):
            TestObject().api_url()

