import unittest
from speedcurve.null import NullObject

class TestNullObject(unittest.TestCase):

    def setUp(self):
        self.instance = NullObject()

    def test_boolean(self):
        assert bool(self.instance) is False

    def test_getattr(self):
        assert self.instance.empty is not None

    def test_str(self):
        assert str(self.instance) == ''
