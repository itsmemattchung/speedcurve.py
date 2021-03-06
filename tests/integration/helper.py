import os
import speedcurve
import betamax

from unittest import TestCase


class IntegrationHelper(TestCase):

    """Base class for all Integration tests."""

    def setUp(self):
        self.api_key = os.environ.get('SPEEDCURVE_API', 'foo')
        self.sc = self.get_client(api_key=self.api_key)
        self.recorder = betamax.Betamax(self.sc.session)

    def cassette_name(self, method_name, cls=None):
        class_name = cls or self.described_class
        return '_'.join([class_name, method_name])

    @property
    def described_class(self):
        class_name = self.__class__.__name__
        return class_name[4:]

    def get_client(self, api_key=None):
        return speedcurve.SpeedCurve(api_key=api_key)
