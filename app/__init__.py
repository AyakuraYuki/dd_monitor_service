# -*- coding: utf-8 -*-

import os

from flask import Flask, redirect, url_for
from flask_babel import Babel
from flask_cors import CORS


def create_app(test_config=None):
    """
    Create a flask application.
    :param test_config: Test configuration
    :return: application instance
    """
    app = Flask(__name__, instance_relative_config=True)
    CORS(app)
    app.config.from_mapping(
        DATABASE=os.path.join(app.instance_path, 'dd_monitor.db'),
        SECRET_KEY='dev' if app.debug else '2c830312-bb99-11e9-8018-6245b50a3dbc',
        LANGUAGES=['zh', 'ja', 'en'],
        BABEL_DEFAULT_LOCALE='en',
    )

    # load the instance config if it is exists, when not testing
    if test_config:
        print(' * Test config detected')
        app.config.from_mapping(test_config)
    else:
        app.config.from_pyfile('config.py', silent=True)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    babel = Babel(app)

    @babel.localeselector
    def get_locale():
        # return request.accept_languages.best_match(app.config['LANGUAGES'])
        from app.const import language
        return language

    # database
    from . import database
    database.init_app(app)

    # router mapping
    @app.route('/')
    def hello():
        # return render_template('index.html')
        return redirect(url_for('monitor.play'))

    # blueprint
    from app.blueprint import dashboard
    from app.blueprint import monitor
    app.register_blueprint(monitor.bp)
    app.register_blueprint(dashboard.bp)

    # blueprint - restful
    from app.api import player_api
    from app.api import link_api
    from app.api import channel_api
    app.register_blueprint(player_api.bp)
    app.register_blueprint(link_api.bp)
    app.register_blueprint(channel_api.bp)

    return app
