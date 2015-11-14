# -*- coding: utf-8 -*-
from .models import SpeedCurveCore


class Site(SpeedCurveCore):
    def _update_attributes(self, site):
        self.name = site.get('name')

    def __repr__(self):
        return '<Site [{0}]>'.format(self.name)
