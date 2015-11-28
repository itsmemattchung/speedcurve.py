"""Speedcurve API."""

from .models import SpeedCurveCore
from .notes import Note
from .sites import Site
from .tests import Test
from .urls import Url
from .deployments import Deployment


class SpeedCurve(SpeedCurveCore):
    """Stored session information."""

    def __init__(self, api_key=None, session=None):
        """Constructor for SpeedCurve.

        :param string api_key: (optional) API key for authentication
        :returns: :class:`SpeedCurve <speedcurve.SpeedCurve>`
        """
        super(SpeedCurve, self).__init__({}, api_key=api_key, session=session)

    def add_deployment(self, site_id=None, note=None, detail=None):
        """Add a deployment and trigger round of testing.

        :param int site_id: (optional) site id to trigger deploy.
        :param string note: (required) short note used on site
        :param string detail: (optional) detail to display for more context
        :returns: :class:`Deployment <speedcurve.deployments.Deployment>`
        """
        data = {
            'site_id': site_id or None,
            'note': str(note) or '',
            'detail': str(detail) or ''
        }

        data = self._remove_none_values(data)

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        url = self._build_url('deploy')
        json = self._json(self._post(url, data=data, headers=headers), 200)
        if json:
            return self._instance_or_null(Deployment, json)

    def get_latest_deployment(self):
        """Retrieve latest deployment.

        :returns: :class:`Deployment <speedcurve.deployments.Deployment>`
        """
        url = self._build_url('deploy', 'latest')
        json = self._json(self._get(url), 200)
        if json:
            return self._instance_or_null(Deployment, json)

    def get_deployment(self, id=None):
        """Retrieve a deployment specified by id.

        :params int id: (required) id of deployment
        :returns: :class:`Deployment <speedcurve.deployments.Deployment>`
        """
        url = self._build_url('deploy', str(id))
        json = self._json(self._get(url), 200)
        if json:
            return self._instance_or_null(Deployment, json)

    def notes(self):
        """Retrieve all notes for main site in User' account.

        :returns: Generator of :class:`Note <speedcurve.notes.Note>`
        """
        url = self._build_url('notes')
        json = self._json(self._get(url), 200)
        if json:
            notes = [
                self._instance_or_null(Note, note) for note in json['notes']
            ]
            return notes

    def sites(self):
        """Retrieve all sites for account."""
        url = self._build_url('sites')
        json = self._json(self._get(url), 200)
        sites = None
        if json:
            sites = [
                self._instance_or_null(Site, s) for s in json.get('sites')
            ]
        return sites

    def test(self, id=None):
        """Retrieve test specified by test id.

        :param string id: (required) ID of test
        :returns: instance of :class:`Test <speedcurve.tests.Test>`
        """
        url = self._build_url('tests', str(id))
        json = self._json(self._get(url), 200)
        if json:
            return self._instance_or_null(Test, json)

    def url(self, id=None, days=30, browser='all'):
        """Retrieve url specified by id.

        :param int id: (required) id of URL
        :param int days: (optional) number of days of tests (max: 365)
        :param string browser: (optional) all, chrome, firefox, ie, or safari
        :returns: :class:`Url <speedcurve.urls.Url>`

        """
        url = self._build_url('urls', str(id))
        params = {
            'days': days,
            'browser': browser
        }
        json = self._json(self._get(url, params=params), 200)
        if json:
            return self._instance_or_null(Url, json)
