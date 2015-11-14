from setuptools import setup

packages = [
    'speedcurve',
    'speedcurve.sites',
    'speedcurve.urls',
    'speedcurve.tests',
    'speedcurve.notes',
    'speedcurve.deployments',
    'speedcurve.errors'
]

setup(
    name='speedcurve.py',
    description=('Python wrapper for Speedcurve API',
                 '(https://api.speedcurve.com/)'),
    author='Matt Chung',
    author_email='itsmemattchung@gmail.com',
    url='https://speedcurvepy.readthedocs.org',
    packages=packages
)
