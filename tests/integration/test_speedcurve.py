"""Integration test for SpeedCurve."""
import speedcurve

from .helper import IntegrationHelper


class TestSpeedcurve(IntegrationHelper):
    """Unit Test for SpeedCurve."""

    def test_add_deployment(self):
        """Test the ability to add deployment and trigger testing."""
        cassette_name = self.cassette_name('add_deployment')
        with self.recorder.use_cassette(cassette_name):
            deployment = self.sc.add_deployment(
                note='speedcurve.py',
                detail='additional details from speedcurve.py'
            )
            assert isinstance(deployment, speedcurve.deployments.Deployment)

    def test_add_deployment_with_site_id(self):
        """Test the ability to add deployment and trigger testing."""
        pass

    def test_notes(self):
        """Test the ability to retrieve notes."""
        cassette_name = self.cassette_name('notes')
        with self.recorder.use_cassette(cassette_name):
            notes = self.sc.notes()
            note = notes[0]
            assert len(notes) > 0
            assert isinstance(note, speedcurve.notes.Note)

    def test_sites(self):
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
            test = self.sc.test(id='151118_QR_a380ad519383d0223518af46f429868e')
            assert isinstance(test, speedcurve.tests.Test)

    def test_get_deployment(self):
        """Test the ability to retrieve deployment specified by id."""
        cassette_name = self.cassette_name('get_deployment')
        with self.recorder.use_cassette(cassette_name):
            deployment = self.sc.get_deployment(id=11627)
            assert isinstance(deployment, speedcurve.deployments.Deployment)

    def test_get_latest_deployment(self):
        """Test the ability to retrieve latest deployment."""
        cassette_name = self.cassette_name('latest_deployment')
        with self.recorder.use_cassette(cassette_name):
            deployment = self.sc.get_latest_deployment()
            assert isinstance(deployment, speedcurve.deployments.Deployment)

    def test_url(self):
        """Test the ability to retrieve url specified by id."""
        cassette_name = self.cassette_name('url')

        with self.recorder.use_cassette(cassette_name):
            url = self.sc.url(id=14419)
            assert isinstance(url, speedcurve.urls.Url)
