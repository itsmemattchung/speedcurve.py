from speedcurve.deployments import Deployment

from .helper import UnitHelper
from .helper import create_example_data_helper

get_example_data = create_example_data_helper('deployment.json')


class TestDeployment(UnitHelper):

    described_class = Deployment
    example_data = get_example_data()

    def test_isinstance(self):
        assert isinstance(self.instance, Deployment)
