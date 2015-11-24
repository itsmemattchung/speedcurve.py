#!/bin/sh

coverage run --source speedcurve -m py.test
coverage report | tail -n 1 | grep '^TOTAL.*100%$'
