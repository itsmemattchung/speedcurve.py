"""Unit test for SpeedCurve."""
from speedcurve import SpeedCurve
from .helper import UnitHelper


class TestSpeedCurve(UnitHelper):
    """Unit test for SpeedCurve."""

    described_class = SpeedCurve

    def test_get_sites(self):
        """Show that user can retrieve sites."""
        self.instance.sites()
        self.session.get.assert_called_once_with(
            'https://api.speedcurve.com/v1/sites'
        )

    def test_get_latest_deployment(self):
        """Show that user can retrieve latest deployment."""
        self.instance.get_latest_deployment()

        self.session.get.assert_called_once_with(
            'https://api.speedcurve.com/v1/deploy/latest'
        )
