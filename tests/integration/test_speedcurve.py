import speedcurve

from .helper import IntegrationHelper


class TestSpeedcurve(IntegrationHelper):

    def def_sites(self):
        """Test the ability to retrieve sites."""

        cassette_name = self.cassette_name('sites')
        with self.recorder.use_cassette(cassette_name):
            sites = self.sc.sites()
            site = sites[0]
            assert len(sites) > 0
            assert isinstance(site, speedcurve.sites.Site)

    def test_test(self):
        """Test the ability to retrieve test specified by id."""

        cassette_name = self.cassette_name('test')
        with self.recorder.use_cassette(cassette_name):
            test = self.sc.test(test_id='151118_QR_a380ad519383d0223518af46f429868e')
            assert isinstance(test, speedcurve.tests.Test)
