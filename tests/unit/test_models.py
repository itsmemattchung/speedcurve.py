"""Unit test for models."""
from speedcurve.models import SpeedCurveCore
from .helper import UnitHelper
from json import loads
from speedcurve.exceptions import AuthenticationFailed
import mock
import pytest


class TestSpeedCurveCore(UnitHelper):
    """Test for speedcurvecore."""

    described_class = SpeedCurveCore
    example_data = '{ "a": "abc" }'

    def test_as_json(self):
        """Show that as_json returns valid json."""
        assert loads(self.instance.as_json()) == self.example_data

    def test_expected_response_raises_authentication_failed(self):
        """Test raised exception for expected_response."""
        response = mock.Mock(status_code=401)
        with pytest.raises(AuthenticationFailed):
            self.instance._expected_response(response, 200, 402)

    def test_expected_response_returns_false(self):
        """Test raised exception for expected_response."""
        assert self.instance._expected_response(None, 200, 402) is False

    def instance_or_null_side_effect(self, *args):
        """Side effect to raise TypeError."""
        if len(args) == 2:
            raise TypeError

    def test_instance_or_null(self):
        """Test instance_or_null raises exceptions."""
        mocker = mock.Mock(side_effect=self.instance_or_null_side_effect)
        instance = self.instance._instance_or_null(instance_class=mocker,
                                                   json=self.example_data)
        assert isinstance(instance, SpeedCurveCore) is False
