"""UNit test for Note."""
import speedcurve
from .helper import UnitHelper
from .helper import create_example_data_helper

get_example_data = create_example_data_helper('note.json')


class TestNote(UnitHelper):
    """Class to test Note."""

    described_class = speedcurve.notes.Note
    example_data = get_example_data()

    def test_repr(self):
        """Show that instance string is formatted correctly."""
        assert repr(self.instance).startswith('<Note')
