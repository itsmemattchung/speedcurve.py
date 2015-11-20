"""Url Class."""
from .models import SpeedCurveCore


class Url(SpeedCurveCore):
    """The :class:`Url <Url>` object."""

    def _update_attributes(self, url):
        self.url = url.get('url')
        self.tests = url.get('tests')

    def __repr__(self):
        return 'Url <speedcurve.urls.Url [{0}]'.format(self.url)
