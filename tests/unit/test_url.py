from speedcurve.urls import Url
from .helper import UnitHelper
from .helper import create_example_data_helper

get_example_data = create_example_data_helper('url.json')


class TestSite(UnitHelper):
    described_class = Url
    example_data = get_example_data()

    def test_isinstance(self):
        assert isinstance(self.instance, Url)

    def test_repr(self):
        instance_string_repr = 'Url <speedcurve.urls.Url [{}]'.format(self.instance.url)
        assert repr(self.instance).startswith(instance_string_repr)
