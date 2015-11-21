"""Unit test for SpeedCurveSession."""
from speedcurve.session import SpeedCurveSession
from unittest import TestCase
import pytest


class TestSpeedCurveSession(TestCase):
    """Class for testing SpeedCurveSession."""

    def test_init(self):
        """Show that ValueError is raised when api_key is not passed."""
        with pytest.raises(ValueError):
            SpeedCurveSession()
