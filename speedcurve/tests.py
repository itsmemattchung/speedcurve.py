# -*- coding: utf-8 -*-
from datetime import datetime
from .models import SpeedCurveCore


class Test(SpeedCurveCore):
    """The :class:`Test <Test>` object."""

    def _update_attributes(self, json):
        self.__dict__.update(json)
        self.__dict__['day'] = datetime.strptime(json['day'], '%Y-%m-%d')
        self.__dict__['timestamp'] = self._strptime(json['timestamp'])

    def __repr__(self):
        return 'Test <speedcurve.tests.Test [{}]>'.format(self.test)
