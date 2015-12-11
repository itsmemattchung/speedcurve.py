from datetime import datetime
from json import dumps
from .session import SpeedCurveSession
from . import exceptions


class SpeedCurveObject(object):
    def __init__(self, json):
        self._update_attributes(json)

    def _update_attributes(self, json):
        pass


class SpeedCurveCore(SpeedCurveObject):

    def __init__(self, json, session=None, api_key=None):

        if hasattr(session, 'session'):
            session = session.session
        elif session is None:
            session = SpeedCurveSession(api_key=api_key)
        self.session = session
        self._as_json = json

        super(SpeedCurveCore, self).__init__(json)

    def as_json(self):
        return dumps(self._as_json)

    def _build_url(self, *args, **kwargs):
        return self.session.build_url(*args, **kwargs)

    def _get(self, url, *args, **kwargs):
        return self.session.get(url, *args, **kwargs)

    def _json(self, response, status_code):
        ret = None

        if self._expected_response(response, status_code, 404):
            ret = response.json()
        return ret

    def _expected_response(self, response, true_code, false_code):
        if response is not None:
            status_code = response.status_code
            if status_code == true_code:
                return True
            if true_code != false_code and status_code >= 400:
                raise exceptions.get_error_for(response)
        return False

    def _instance_or_null(self, instance_class=None, json=None):
        try:
            return instance_class(json, self)
        except TypeError:
            return instance_class(json)

    def _remove_none_values(self, dictionary):
        """Helper method to remove None values from dictionary."""
        data = dictionary.copy()
        if not data:
            return
        for key, value in data.items():
            if value is None:
                del(data[key])
        return data

    def _post(self, url, *args, **kwargs):
        return self.session.post(url, *args, **kwargs)

    def _strptime(self, time_str):
        return datetime.utcfromtimestamp(time_str)
