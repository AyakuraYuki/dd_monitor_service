#!/usr/bin/env bash
export FLASK_APP=run.py
flask init-schemas
python run.py
