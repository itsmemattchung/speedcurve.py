from speedcurve.tests import Test
from .helper import UnitHelper
from .helper import create_example_data_helper

get_example_data = create_example_data_helper('test.json')


class TestTest(UnitHelper):

    example_data = get_example_data()
    described_class = Test

    def test_isinstance(self):
        assert isinstance(self.instance, Test)

    def test_repr(self):
        assert repr(self.instance).startswith('Test <speedcurve.tests.Test')
