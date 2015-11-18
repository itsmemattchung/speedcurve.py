from setuptools import setup
from speedcurve import __version__

packages = [
    'speedcurve',
]

setup(
    author='Matt Chung',
    author_email='itsmemattchung@gmail.com',
    description=('Python wrapper for Speedcurve API',
                 '(https://api.speedcurve.com/)'),
    install_requires=[
        'requests'
    ],
    name='speedcurve.py',
    url='https://speedcurvepy.readthedocs.org',
    packages=packages,
    version=__version__
)
