from speedcurve.deployments import Deployment

from .helper import UnitHelper
from .helper import create_example_data_helper

get_example_data = create_example_data_helper('deployment.json')


class TestDeployment(UnitHelper):

    described_class = Deployment
    example_data = get_example_data()

    def test_id(self):
        assert self.instance.id is not None

    def test_attributes(self):
        attributes = (
            'id',
            'tests_completed',
            'status',
            'tests_remaining',
            'note',
            'detail'
        )

        for attribute in attributes:
            assert hasattr(self.instance, attribute)

    def test_isinstance(self):
        assert isinstance(self.instance, Deployment)

    def test_repr(self):
        assert repr(self.instance).startswith('<Deployment')
