#!/usr/bin/env bash
export FLASK_APP=run-dd-monitor.py
flask init-schemas
python run-dd-monitor.py
