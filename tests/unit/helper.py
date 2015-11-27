try:
    from unittest import mock
except ImportError:
    import mock
import os
import json
import unittest
import speedcurve
from speedcurve.session import SpeedCurveSession


def build_url(self, *args, **kwargs):
    return speedcurve.session.SpeedCurveSession(api_key='').build_url(*args, **kwargs)


def create_example_data_helper(example_filename):
    example_data_directory = 'example_data'
    example_data_path = os.path.join(os.path.dirname(__file__),
                                     example_data_directory,
                                     example_filename)

    def data_helper():
        with open(example_data_path) as fd:
            data = json.load(fd)
            return data

    return data_helper


class UnitHelper(unittest.TestCase):
    """Base class for unittest."""

    described_class = None
    example_data = None

    def create_instance_of_described_class(self):
        if self.example_data:
            instance = self.described_class(self.example_data,
                                            self.session)
        else:
            instance = self.described_class(api_key='', session=self.session)

        return instance

    def create_mocked_session(self):
        session = mock.create_autospec(SpeedCurveSession)
        session.get.return_value = None
        session.put.return_value = None
        return session

    def setUp(self):
        self.session = self.create_mocked_session()
        self.described_class._build_url = build_url
        self.instance = self.create_instance_of_described_class()

    def tearDown(self):
        pass
