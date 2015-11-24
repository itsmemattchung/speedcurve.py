"""Unit test for Site."""
from .helper import UnitHelper
from .helper import create_example_data_helper
from speedcurve.sites import Site

get_example_data = create_example_data_helper('site.json')


class TestSite(UnitHelper):
    """Class to test Site."""

    described_class = Site
    example_data = get_example_data()

    def test_attributes(self):
        """Show attributes exist in class."""
        attributes = [
            'id',
            'median',
            'name',
            'urls'
        ]

        for attribute in attributes:
            assert getattr(self.instance, attribute)

    def test_repr(self):
        """Show that instance string is formatted correctly."""
        assert repr(self.instance).startswith('<Site [')
