missing = object()

class ObjectMeta(type):

    def __new__(meta, name, bases, __dict__):
        field_names = __dict__['field_names'] = []
        if name != 'Object':
            for key, obj in __dict__.items():
                if isinstance(obj, Field):
                    field_names.append(key)

        cls = super(ObjectMeta, meta).__new__(meta, name, bases, __dict__)

        if name != 'Object':
            cls.registry[cls.code] = cls

        return cls


class Object(object):

    __metaclass__ = ObjectMeta
    registry = {}

    def __init__(self, session=None, **fields):
        self.session = session
        self.fields = fields

    def __repr__(self):
        return '<{0}: {1}>'.format(self.__class__.__name__,
                                   self.fields)

    @classmethod
    def from_data(cls, session, data):
        return cls.registry[data['objCode']](session, **data)

    @classmethod
    def field_spec(cls, *field_names):
        workfront_fields = []
        for field_name in field_names:
            field = getattr(cls, field_name, None)
            if field is None:
                workfront_fields.append(field_name)
            else:
                workfront_fields.append(field.workfront_name)
        return ','.join(workfront_fields)

    def load(self, *field_names):
        fields = self.session.get(self.api_url(),
                                  dict(fields=self.field_spec(*field_names)))
        self.fields.update(fields)

    def api_url(self):
        return '/{0}/{1}'.format(self.code, self.id)

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