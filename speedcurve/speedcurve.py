"""Speedcurve API"""

from .models import SpeedCurveCore
from .sites import Site
from .urls import Url


class SpeedCurve(SpeedCurveCore):

    def __init__(self, api_key=None):
        super(SpeedCurve, self).__init__({}, api_key=api_key)

    def url(self, id=None, days=30, browser='all'):
        url = self.session.build_url('urls', str(id))
        params = {
            'days': days,
            'browser': browser
        }
        json = self._json(self._get(url, params=params))
        return self._instance_or_null(Url, json)

    def sites(self):
        url = self.session.build_url('sites')
        json = self._json(self._get(url))
        sites = [self._instance_or_null(Site, site) for site in json['sites']]
        return sites
