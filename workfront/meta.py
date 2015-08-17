missing = object()

class ObjectMeta(type):

    def __new__(meta, name, bases, __dict__):
        field_names = __dict__['field_names'] = []
        if name != 'Object':
            for key, obj in __dict__.items():
                if isinstance(obj, Field):
                    field_names.append(key)

        cls = super(ObjectMeta, meta).__new__(meta, name, bases, __dict__)

        return cls


class Object(object):

    __metaclass__ = ObjectMeta

    def __init__(self, session=None, **fields):
        self.session = session
        self.fields = fields

    def __repr__(self):
        return '<{0}: {1}>'.format(self.__class__.__name__,
                                   self.__dict__)

    def load(self, *fields):
        workfront_fields = []
        for field_name in fields:
            field = getattr(self.__class__, field_name, None)
            if field is None:
                workfront_fields.append(field_name)
            else:
                workfront_fields.append(field.workfront_name)
        fields = self.session.get('/{0}/{1}'.format(self.code, self.id),
                                  dict(fields=','.join(workfront_fields)))
        self.fields.update(fields)


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