class Object(object):

    def __init__(self, session=None, ID=None, **fields):
        self.session = session
        self.ID = ID
        self.__dict__.update(fields)

    def __repr__(self):
        return '<{0}: {1}>'.format(self.__class__.__name__,
                                   self.__dict__)

