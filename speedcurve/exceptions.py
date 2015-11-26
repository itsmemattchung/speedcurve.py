"""All exceptions for speedcurve library."""


class SpeedCurveError(Exception):
    """The base exception class."""

    def __init__(self, response):
        super(SpeedCurveError, self).__init__(response)
        self.response = response
        self.code = response.status_code
        self.errors = []

        try:
            error = response.json()
            self.errors = error.get('errors')
        except:
            self.msg = response.content or '[No Message]'


class AuthenticationFailed(SpeedCurveError):
    pass


class BadRequest(SpeedCurveError):
    pass


class ForbiddenError(SpeedCurveError):
    pass


class NotFoundError(SpeedCurveError):
    pass

error_classes = {
    400: BadRequest,
    401: AuthenticationFailed,
    403: ForbiddenError,
    404: NotFoundError
}


def get_error_for(response):
    """Return initialized exception."""
    status_code = response.status_code
    error_class = error_classes.get(status_code)
    return error_class(response)
