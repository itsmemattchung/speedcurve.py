"""Unit Test for models."""
import speedcurve
from .helper import UnitHelper
from json import loads


class TestSpeedCurveCore(UnitHelper):
    """Unit Test for SpeedCurveCore."""

    described_class = speedcurve.models.SpeedCurveCore
    example_data = '{ "a": "abc" }'

    def test_as_json(self):
        """Show as_json returns valid json."""
        assert loads(self.instance.as_json()) == self.example_data
