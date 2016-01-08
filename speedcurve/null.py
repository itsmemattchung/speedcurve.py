class NullObject(object):
    """NullObject intended for empty JSON responses."""

    def __init__(self, initializer=None):
        self.__dict__['initializer'] = initializer

    def __bool__(self):
        return False

    __nonzero__ = __bool__

    def __getattr__(self, attr):
        return self

    def __str__(self):
        return ''
