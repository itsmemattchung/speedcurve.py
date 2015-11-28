"""Unit test for SpeedCurve."""
from speedcurve import SpeedCurve
from .helper import UnitHelper


class TestSpeedCurve(UnitHelper):
    """Unit test for SpeedCurve."""

    described_class = SpeedCurve

    def test_add_deployment(self):
        """Show that user can add a deployment."""
        note = 'speedcurve.py'
        detail = 'additional details'
        self.instance.add_deployment(
            note=note,
            detail=detail
        )
        self.session.post.assert_called_once_with(
            'https://api.speedcurve.com/v1/deploy',
            data={
                'note': note,
                'detail': detail
            },
            headers={
                'Content-Type': 'application/x-www-form-urlencoded'
            }
        )

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
