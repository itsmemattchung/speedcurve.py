"""Unit test for exceptions."""
from unittest import TestCase
from speedcurve.exceptions import get_error_for
from speedcurve.exceptions import AuthenticationFailed
import mock


class TestExceptions(TestCase):

    def test_get_error_for(self):
        """Test that an AuthenticationFailed is returned."""
        response = mock.Mock(status_code=401, content='')
        error = get_error_for(response)
        assert isinstance(error, AuthenticationFailed)
        response.json.side_effect = Exception
        error = get_error_for(response)
        assert error.msg == '[No Message]'
