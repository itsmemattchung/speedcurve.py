"""Speedcurve API"""

from .models import SpeedCurveCore
from .sites import Site


class SpeedCurve(SpeedCurveCore):

    def __init__(self, api_key=None):
        super(SpeedCurve, self).__init__({}, api_key=api_key)

    def sites(self):
        url = self.session.build_url('sites')
        json = self._json(self._get(url))
        sites = [self._instance_or_null(Site, site) for site in json['sites']]
        return sites
