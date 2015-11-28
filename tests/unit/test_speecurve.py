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

    def test_get_deployment(self):
        """Show that user can retrieve a specific deployment."""
        self.instance.get_deployment(id=1)

        self.session.get.assert_called_once_with(
            'https://api.speedcurve.com/v1/deploy/1'
        )

    def test_notes(self):
        """Show that a user can retrieve notes."""
        self.instance.notes()

        self.session.get.assert_called_once_with(
            'https://api.speedcurve.com/v1/notes'
        )

    def test_test(self):
        """Show that a user can retrieve a test specified by id."""
        self.instance.test(id=1)

        self.session.get.assert_called_once_with(
            'https://api.speedcurve.com/v1/tests/1'
        )

    def test_url(self):
        """Show that that a user can retrieve a url."""
        self.instance.url(id=1, days=1, browser='chrome')

        self.session.get.assert_called_once_with(
            'https://api.speedcurve.com/v1/urls/1',
            params={
                'days': 1,
                'browser': 'chrome'
            }
        )
