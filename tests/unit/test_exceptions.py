"""Unit test for exceptions."""
from unittest import TestCase
from speedcurve.exceptions import get_error_for
from speedcurve.exceptions import AuthenticationFailed
from speedcurve.exceptions import BadRequest
from speedcurve.exceptions import ForbiddenError
from speedcurve.exceptions import NotFoundError
import mock


class TestExceptions(TestCase):
    """Exception unit test."""

    def test_get_error_for(self):
        """Test that an AuthenticationFailed is returned."""
        response = mock.Mock(status_code=401, content='')
        error = get_error_for(response)
        assert isinstance(error, AuthenticationFailed)
        response.json.side_effect = Exception
        error = get_error_for(response)
        assert error.msg == '[No Message]'

    def test_forbidden_error(self):
        """Test that a ForbiddenError is raised."""
        response = mock.Mock(status_code=403)
        error = get_error_for(response)
        assert isinstance(error, ForbiddenError)

    def test_bad_request_error(self):
        """Test that a BadRequest error is raised."""
        response = mock.Mock(status_code=400)
        error = get_error_for(response)
        assert isinstance(error, BadRequest)

    def test_not_found_error(self):
        """Test that a NotFoundError is raised."""
        response = mock.Mock(status_code=404)
        error = get_error_for(response)
        assert isinstance(error, NotFoundError)
