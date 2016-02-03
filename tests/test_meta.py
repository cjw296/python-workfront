from unittest import TestCase

from testfixtures import compare, ShouldRaise, Comparison as C

from tests.test_session import MockOpenHelper
from workfront import Session
from workfront.meta import APIVersion, Object, Field, FieldNotLoaded, Reference


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

    def make_test_object(self):
        class TestObject(Object):
            code='TEST'
            field_one = Field('fieldOne')
            field_two = Field('fieldTwo')
        return TestObject

    def test_field_names(self):
        TestObject = self.make_test_object()
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

    def test_load(self):
        TestObject = self.make_test_object()

        obj = TestObject(Session('test'), ID='x')
        obj.field_one = 1
        obj.field_two = 2

        compare(obj.fields.dirty(), {'fieldOne': 1, 'fieldTwo': 2})

        self.server.add(
            url='/TEST/x',
            params='fields=fieldOne&method=GET',
            response='{"data":{"fieldOne": 3}}')

        obj.load('field_one')

        compare(obj.field_one, expected=3)
        compare(obj.fields.dirty(), {'fieldTwo': 2})

    def test_save_create(self):
        TestObject = self.make_test_object()
        obj = TestObject(Session('test'),
                         field_one = 1,
                         field_two = 2)

        self.server.add(
            url='/TEST',
            params='method=POST&fieldOne=1&fieldTwo=2',
            response='{"data":{"ID": "y"}}')

        obj.save()

        compare(obj.id, 'y')
        compare(obj.fields.dirty(), {})

    def test_save_update(self):
        # some dirty, some not, check clean results
        TestObject = self.make_test_object()
        obj = TestObject(Session('test'), ID='x')
        obj.field_one = 1

        self.server.add(
            url='/TEST/x',
            params='method=PUT&fieldOne=1',
            response='{"data": null}')

        obj.save()

        compare(obj.id, 'x')
        compare(obj.fields.dirty(), {})

    def test_save_no_dirty(self):
        TestObject = self.make_test_object()
        obj = TestObject(Session('test'), ID='x')

        # no post!
        obj.save()

        compare(obj.id, 'x')
        compare(obj.fields.dirty(), {})

    def test_delete(self):
        TestObject = self.make_test_object()
        obj = TestObject(Session('test'), ID='x')

        self.server.add(
            url='/TEST/x',
            params='method=DELETE',
            response='{"data": null}')

        obj.delete()

        self.server.assert_called(times=1)

    def test_bad_field(self):
        TestObject = self.make_test_object()
        obj = TestObject()
        with ShouldRaise(AttributeError(
            "'TestObject' object has no attribute 'bad_field'"
        )):
            obj.bad_field = 'foo'


class LoadingAttributeTests(MockOpenHelper, TestCase):

    base = 'https://test.attask-ondemand.com/attask/api/test'

    def setUp(self):
        super(LoadingAttributeTests, self).setUp()
        self.replace('workfront.session.Session.version_registry', {})
        test_api = APIVersion('test')
        class TestObject(Object):
            code='TEST'
            field_one = Field('fieldOne')
            field_two = Field('fieldTwo')
        test_api.register(TestObject)
        Session.register(test_api)
        self.session = Session('test', api_version='test')

    def test_reference(self):
        class AnotherObject(Object):
            code='OTHER'
            ref_field = Reference('refField')

        obj = AnotherObject(self.session,
                            refField=dict(objCode='TEST', fieldOne='foo'))

        ref_obj = obj.ref_field
        compare(ref_obj.field_one, expected='foo')
        with ShouldRaise(FieldNotLoaded('fieldTwo')):
            ref_obj.field_two

    def test_reference_not_loaded(self):
        class AnotherObject(Object):
            code='OTHER'
            ref_field = Reference('refField')

        obj = AnotherObject(self.session, ID='xxx')

        self.server.add(
            url='/OTHER/xxx',
            params='method=GET&fields=refField',
            response='{"data": {"refField": '
                     '{"objCode": "TEST", "ID": "yyy", '
                     '"fieldOne":1, "fieldTwo":2}}}'
        )

        ref_obj = obj.ref_field
        compare(ref_obj.id, expected='yyy')
        compare(ref_obj.field_one, expected=1)
        compare(ref_obj.field_two, expected=2)

    def test_reference_from_class(self):
        class AnotherObject(Object):
            ref_field = Reference('refField')

        compare(AnotherObject.ref_field,
                expected=C(Reference, workfront_name='refField'))

    def test_reference_modify(self):
        class AnotherObject(Object):
            ref_field = Reference('refField')

        obj = AnotherObject()

        with ShouldRaise(AttributeError('Reference cannot be set')):
            obj.ref_field = 'foo'
