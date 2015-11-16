from .session import SpeedCurveSession


class SpeedCurveObject(object):
    def __init__(self, json):
        self._update_attributes(json)

    def _update_attributes(self, json):
        pass

class SpeedCurveCore(SpeedCurveObject):

    def __init__(self, json, api_key=None, session=None):

        if hasattr(session, 'session'):
            session = session.session
        elif session is None:
            session = SpeedCurveSession(api_key=api_key)
        self.session = session

        super(SpeedCurveCore, self).__init__(json)

    def _get(self, url, *args, **kwargs):
        return self.session.get(url, *args, **kwargs)

    def _json(self, response):
        return response.json()

    def _instance_or_null(self, instance_class=None, json=None):
        try:
            return instance_class(json, self)
        except TypeError:
            return instance_class(json)
