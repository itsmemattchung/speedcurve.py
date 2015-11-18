import os
import base64
import speedcurve
import betamax

from unittest import TestCase


class IntegrationHelper(TestCase):

    """Base class for all Integration tests."""

    def setUp(self):
        self.api_key = os.environ['SPEEDCURVE_API']
        self.basic_auth = b':'.join([self.api_key, 'x'])
        self.sc = self.get_client(api_key=self.api_key)
        self.recorder = betamax.Betamax(self.sc.session)
        self.configure_betamax()

    def cassette_name(self, method_name, cls=None):
        class_name = cls or self.described_class
        return '_'.join([class_name, method_name])

    def configure_betamax(self):
        with betamax.Betamax.configure() as config:
            config.cassette_library_dir = 'tests/cassettes'
            config.default_cassette_options['record_mode'] = 'once'
            config.define_cassette_placeholder(
                '<BASIC_AUTH>',
                base64.b64encode(self.basic_auth).decode()
            )

    @property
    def described_class(self):
        class_name = self.__class__.__name__
        return class_name[4:]

    def get_client(self, api_key=None):
        return speedcurve.SpeedCurve(api_key=api_key)
