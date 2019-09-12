#!/usr/bin/env bash
export FLASK_APP=app/run.py
export FLASK_RUN_PORT=5140
export FLASK_ENV=production
export FLASK_DEBUG=0
flask run
