"""Integration test for SpeedCurve exceptions."""
import speedcurve
import pytest

from .helper import IntegrationHelper
from speedcurve.exceptions import ForbiddenError


class TestExceptions(IntegrationHelper):
    """Integration test for Exceptions."""

    def test_add_deployment_while_other_in_progress(self):
        """Test that an error is raised when deployment in progress."""
        cassette_name = self.cassette_name('add_deployment_success')
        note = 'speedcurve.py'
        detail = 'additional details from speedcurve.py'
        with self.recorder.use_cassette(cassette_name):
            deployment = self.sc.add_deployment(
                note=note,
                detail=detail
            )

            assert isinstance(deployment, speedcurve.deployments.Deployment)

        cassette_name = self.cassette_name('add_deployment_in_progress')
        with self.recorder.use_cassette(cassette_name):

            with pytest.raises(ForbiddenError):
                deployment = self.sc.add_deployment(
                    note=note,
                    detail=detail
                )
