# -*- coding: utf-8 -*-
from .models import SpeedCurveCore


class Test(SpeedCurveCore):
    """The :class:`Test <Test>` object. """

    def _update_attributes(self, json):
        self.browser = json.get('browser')
        self.browser_version = json.get('browser_version')
        self.byte = json.get('byte')
        self.css_requests = json.get('css_requests')
        # TODO: change to datetime object
        self.day = json.get('day')
        self.flash_requests = json.get('flash_requests')
        self.font_requests = json.get('font_requests')
        self.font_size = json.get('font_size')
        self.har = json.get('har')
        self.html_requests = json.get('html_requests')
        self.html_size = json.get('html_size')
        self.image_requests = json.get('image_requests')
        self.image_saving = json.get('image_saving')
        self.image_size = json.get('image_size')
        self.js_requests = json.get('js_requests')
        self.js_size = json.get('js_size')
        self.loaded = json.get('loaded')
        self.other_requests = json.get('other_requests')
        self.other_size = json.get('other_size')
        self.pagespeed = json.get('pagespeed')
        self.render = json.get('render')
        self.requests = json.get('requests')
        self.run = json.get('run')
        self.screen = json.get('screen')
        self.size = json.get('size')
        self.speedindex = json.get('speedindex')
        self.test = json.get('test')
        self.text_requests = json.get('text_requests')
        self.timestamp = json.get('timestamp')
        self.timezone = json.get('timezone')

    def __repr__(self):
        return 'Test <speedcurve.tests.Test [{}]>'.format(self.test)
