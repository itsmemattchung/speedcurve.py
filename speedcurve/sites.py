# -*- coding: utf-8 -*-
from .models import SpeedCurveCore


class Site(SpeedCurveCore):
    """The :class:`Site <Site>` object. """

    def _update_attributes(self, site):
        self.id = site.get('site_id')
        self.name = site.get('name')
        self.median = site.get('median')
        self.urls = site.get('urls')

    def __repr__(self):
        return '<Site [{0}]>'.format(self.name)
