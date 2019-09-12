# -*- coding: utf-8 -*-

import os

from flask import Flask, render_template
from flask_cors import CORS


def create_app(test_config=None):
    """
    Create a flask application.
    :param test_config: Test configuration
    :return: application instance
    """
    prepare_app = Flask(__name__, instance_relative_config=True)
    CORS(prepare_app)

    prepare_app.config.from_mapping(
        DATABASE=os.path.join(prepare_app.instance_path, 'dd_monitor.db'),
    )

    # ensure the instance folder exists
    try:
        os.makedirs(prepare_app.instance_path)
    except OSError:
        pass

    # load the instance config if it is exists, when not testing
    if test_config:
        print(' * Test config detected')
        prepare_app.config.from_mapping(test_config)
    else:
        prepare_app.config.from_pyfile('config.py', silent=True)

    # database
    from . import database
    database.init_app(prepare_app)

    # blueprint - restful
    from .api import rest
    from .api import player_api
    from .api import link_api
    from .api import vue_api
    prepare_app.register_blueprint(rest)
    prepare_app.register_blueprint(link_api.bp)
    prepare_app.register_blueprint(player_api.bp)
    prepare_app.register_blueprint(vue_api.bp)

    # web entry
    @prepare_app.route('/')
    def index():
        return render_template('index.html')

    return prepare_app


app = create_app()

if __name__ == '__main__':
    app.run(
        port=5140
    )
