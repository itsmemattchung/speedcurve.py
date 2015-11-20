"""Speedcurve API"""

from .models import SpeedCurveCore
from .sites import Site
from .tests import Test
from .urls import Url
from .deployments import Deployment


class SpeedCurve(SpeedCurveCore):

    def __init__(self, api_key=None):
        super(SpeedCurve, self).__init__({}, api_key=api_key)

    def add_deployment(self, note=None, detail=None):
        """Add a deployment and trigger round of testing.

        :param string note: (required) short note used on site
        :param string detail: (optional) detail to display for more context
        :returns: :class:`Deployment <speedcurve.deployments.Deployment>`
        """
        data = {
            'note': str(note) or '',
            'detail': str(detail) or ''
        }

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        url = self.session.build_url('deploy')
        json = self._json(self._post(url, data=data, headers=headers), 200)
        return self._instance_or_null(Deployment, json)

    def get_latest_deployment(self):
        """Retrieve latest deployment

        :returns: :class:`Deployment <speedcurve.deployments.Deployment>`
        """
        url = self.session.build_url('deploy', 'latest')
        json = self._json(self._get(url), 200)
        return self._instance_or_null(Deployment, json)

    def get_deployment(self, id=None):
        """Retrieve a deployment specified by id

        :params int id: (required) id of deployment
        :returns: :class:`Deployment <speedcurve.deployments.Deployment>`
        """
        url = self.session.build_url('deploy', str(id))
        json = self._json(self._get(url), 200)
        return self._instance_or_null(Deployment, json)

    def sites(self):
        """Retrieve all sites for account"""
        url = self.session.build_url('sites')
        json = self._json(self._get(url), 200)
        sites = [self._instance_or_null(Site, site) for site in json['sites']]
        return sites

    def test(self, id=None):
        """Retrieve test specified by test id

        :param string id: (required) ID of test
        :returns: instance of :class:`Test <speedcurve.tests.Test>`
        """
        url = self.session.build_url('tests', str(id))
        json = self._json(self._get(url), 200)
        return self._instance_or_null(Test, json)

    def url(self, id=None, days=30, browser='all'):
        """Retrieve url specified by id

        :param int id: (required) id of URL
        :param int days: (optional) number of days of tests (max: 365)
        :param string browser: (optional) all, chrome, firefox, ie, or safari
        :returns: generator of :class:`Url <speedcurve.urls.Url>`

        """
        url = self.session.build_url('urls', str(id))
        params = {
            'days': days,
            'browser': browser
        }
        json = self._json(self._get(url, params=params))
        return self._instance_or_null(Url, json)
