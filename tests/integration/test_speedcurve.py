import speedcurve

from .helper import IntegrationHelper


class TestSpeedcurve(IntegrationHelper):

    def test_sites(self):
        """Test the ability to retrieve sites."""

        cassette_name = self.cassette_name('sites')
        with self.recorder.use_cassette(cassette_name):
            sites = self.sc.sites()
            site = sites[0]
            assert len(sites) > 0
            assert isinstance(site, speedcurve.sites.Site)
