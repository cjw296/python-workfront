from workfront.six import with_metaclass

missing = object()


class APIVersion(object):

    def __init__(self, version):
        self.version = version
        self.by_code = {}

    def register(self, type_):
        setattr(self, type_.__name__, type_)
        self.by_code[type_.code] = type_

    def override(self, type_, replacement):
        setattr(self, type_.__name__, replacement)
        self.by_code[type_.code] = replacement

    def from_data(self, session, data):
        return self.by_code[data['objCode']](session, **data)


class FieldNotLoaded(Exception):
    pass


class Field(object):

    def __init__(self, workfront_name):
        self.workfront_name = workfront_name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        result = instance.fields.get(self.workfront_name, missing)
        if result is missing:
            raise FieldNotLoaded(self.workfront_name)
        return result

    def __set__(self, instance, value):
        instance.fields[self.workfront_name] = value


class LoadingAttribute(object):

    def __init__(self, workfront_name):
        self.workfront_name = workfront_name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        if self.workfront_name not in instance.fields:
            instance.load(self.workfront_name)
        session = instance.session
        api = session.api
        return self.process(session, api, instance.fields[self.workfront_name])

    def __set__(self, instance, value):
        raise AttributeError(self.__class__.__name__ + ' cannot be set')


class Reference(LoadingAttribute):

    @staticmethod
    def process(session, api, data):
        return api.from_data(session, data)


class Collection(LoadingAttribute):

    @staticmethod
    def process(session, api, data):
        return tuple(api.from_data(session, object_data)
                     for object_data in data)


class ModificationTrackingDict(dict):

    def __init__(self):
        self.clean()

    def clean(self, only=None):
        if only:
            for key in only:
                self.dirty_keys.discard(key)
        else:
            self.dirty_keys = set()

    def __setitem__(self, key, value):
        super(ModificationTrackingDict, self).__setitem__(key, value)
        self.dirty_keys.add(key)

    def dirty(self):
        data = {}
        for key in self.dirty_keys:
            data[key] = self[key]
        return data


class ObjectMeta(type):

    def __new__(meta, name, bases, __dict__):
        field_names = set()
        for key, obj in __dict__.items():
            if isinstance(obj, Field):
                field_names.add(key)
        __dict__['__slots__'] = ('session', 'fields')
        cls = super(ObjectMeta, meta).__new__(meta, name, bases, __dict__)
        cls.field_names = getattr(cls, 'field_names', set()) | field_names
        return cls


class Object(with_metaclass(ObjectMeta, object)):

    registry = {}

    def __init__(self, session=None, **fields):
        self.session = session
        self.fields = ModificationTrackingDict()
        for name, value in fields.items():
            if name in self.field_names:
                setattr(self, name, value)
            else:
                self.fields[name] = value
        self.fields.clean()

    def __repr__(self):
        return '<{0}: {1}>'.format(
            self.__class__.__name__,
            ', '.join('{}={!r}'.format(f, v)
                      for (f, v) in sorted(self.fields.items()))
        )

    @property
    def id(self):
        return self.fields.get('ID')

    @classmethod
    def convert_name(cls, field_name):
        if isinstance(field_name, Field):
            return field_name.workfront_name
        field = getattr(cls, field_name, None)
        if field is None:
            return field_name
        else:
            return field.workfront_name

    @classmethod
    def field_spec(cls, *field_names):
        workfront_fields = []
        for field_name in field_names:
            workfront_fields.append(cls.convert_name(field_name))
        return ','.join(workfront_fields)

    def api_url(self):
        if not self.id:
            raise ValueError('{0} has no ID'.format(self.__class__.__name__))
        return '/{0}/{1}'.format(self.code, self.id)

    def load(self, *field_names):
        fields = self.session.get(self.api_url(),
                                  dict(fields=self.field_spec(*field_names)))
        self.fields.update(fields)
        self.fields.clean(fields)

    def save(self):
        if self.id is None:
            data = self.session.post('/'+self.code, self.fields)
            self.fields.update(data)
        else:
            dirty = self.fields.dirty()
            if dirty:
                self.session.put(self.api_url(), dirty)
        self.fields.clean()

    def delete(self):
        self.session.delete(self.api_url())
