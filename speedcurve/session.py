# -*- coding: utf-8 -*-
import requests


class SpeedCurveSession(requests.Session):

    def __init__(self, api_key=None):
        if api_key is None:
            raise ValueError("API Key Required")

        self.api_key = str(api_key)
        self.basic_authentication = (str(self.api_key), 'x')
        super(SpeedCurveSession, self).__init__()
        self.headers.update({
            'Content-Type': 'application/json'
        })
        self.base_url = 'https://api.speedcurve.com/v1'

    def build_url(self, *args, **kwargs):
        parts = [kwargs.get('base_url') or self.base_url]
        parts.extend(args)
        url = '/'.join(parts)
        return url

    def get(self, *args, **kwargs):
        kwargs['auth'] = self.basic_authentication
        return super(SpeedCurveSession, self).get(*args, **kwargs)

    def post(self, *args, **kwargs):
        kwargs['auth'] = self.basic_authentication
        return super(SpeedCurveSession, self).post(*args, **kwargs)
