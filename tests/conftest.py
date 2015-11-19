import os
import base64
import betamax

api_key = os.environ.get('SPEEDCURVE_API', 'foo')
basic_auth = b':'.join([api_key, 'bar'])

with betamax.Betamax.configure() as config:
    config.cassette_library_dir = 'tests/cassettes'
    config.default_cassette_options['record_mode'] = 'once'
    config.define_cassette_placeholder(
        '<BASIC_AUTH>',
        base64.b64encode(basic_auth).decode()
    )
