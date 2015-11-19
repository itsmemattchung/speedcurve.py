class SpeedCurveError(Exception):
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

error_classes = {
    401: AuthenticationFailed
}


def get_error_for(response):
    """Return initialized exception."""
    status_code = response.status_code
    error_class = error_classes.get(status_code)
    return error_class(response)
