"""Unit Test for models."""
import speedcurve
import mock
from .helper import UnitHelper
from json import loads


class TestSpeedCurveCore(UnitHelper):
    """Unit Test for SpeedCurveCore."""

    described_class = speedcurve.models.SpeedCurveCore
    example_data = '{ "a": "abc" }'

    def test_as_json(self):
        """Show as_json returns valid json."""
        assert loads(self.instance.as_json()) == self.example_data

    def test_expected_response_404(self):
        """Verify exception is not raised for 404."""
        response = mock.Mock(status=404)
        assert self._expected_response(response, 200, 404) is False
