missing = object()

class ObjectMeta(type):

    def __new__(meta, name, bases, __dict__):
        if name != 'Object':
            field_names = set()
            for key, obj in __dict__.items():
                if isinstance(obj, Field):
                    field_names.add(key)

        cls = super(ObjectMeta, meta).__new__(meta, name, bases, __dict__)

        if name != 'Object':
            cls.registry[cls.code] = cls
            cls.field_names = getattr(cls, 'field_names', set()) | field_names

        return cls


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


class Object(object):

    __metaclass__ = ObjectMeta
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
        return '<{0}: {1}>'.format(self.__class__.__name__,
                                   self.fields)

    @property
    def id(self):
        return self.fields.get('ID')

    @classmethod
    def from_data(cls, session, data):
        return cls.registry[data['objCode']](session, **data)

    @classmethod
    def convert_name(cls, field_name):
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
            self.session.put(self.api_url(), self.fields.dirty())
        self.fields.clean()

    def delete(self):
        self.session.delete(self.api_url())


class FieldNotLoaded(AttributeError):
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


class Reference(object):

    def __init__(self, workfront_name, code):
        self.workfront_name = workfront_name
        self.code = code

    def __get__(self, instance, owner):
        if instance is None:
            return self
        result = instance.fields.get(self.workfront_name, missing)
        if result is missing:
            id_ = instance.fields.get(self.workfront_name+'ID', missing)
            if id_ is missing:
                raise FieldNotLoaded(self.workfront_name)
            if id_ is None:
                result = None
            else:
                result = dict(ID=id_, objCode=self.code)
        if result is None:
            return None
        return Object.from_data(instance.session, result)
