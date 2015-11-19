speedcurve
=============

.. image:: https://travis-ci.org/itsmemattchung/speedcurve.py.svg?branch=master

A wrapper for around the `SpeedCurve API v1`_

`Full documentation`_

Example Use
-----------

.. code-block:: python

   from speedcurve import SpeedCurve

   sc = SpeedCurve(api_key='your-api-key-here')
   # Get all sites for a user
   sites = sc.sites()

   # Get trends and all tests for a URL
   urls = sc.urls()

   # Get trends and chrome tests for a URL
   urls = sc.urls(browser='chrome')

   # Get a test
   test = sc.test(id='140317_BA_3W8')

   # Get all the notes for the main site
   notes = sc.notes()

   # Add a note. Timestamp defaults to now()
   note = sc.create_note(
       note="Cleared CDN Cache",
       detail="Testing origin response times"
   )

   # Add a deployment
   sc.create_deployment(
       note="Code deployment",
       detail="Triggered a deployment to test session capability"
   )

Testing
-------

Run :code:`pip install -r dev-requirements.txt`.  You can then execute :code:`tox`.

.. _SpeedCurve API v1 : https://api.speedcurve.com/
.. _Full documentation: http://speedcurvepy.readthedocs.org/
