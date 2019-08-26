# -*- coding: utf-8 -*-

import os
import sqlite3

from DBUtils.PersistentDB import PersistentDB
from flask import Flask, render_template
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
        SECRET_KEY='dev' if app.debug else '8428bc0d90194a9787e838c96596a6bb',
        LANGUAGES=['zh', 'ja', 'en'],
        BABEL_DEFAULT_LOCALE='en',
        DBCP=PersistentDB(
            creator=sqlite3,
            database=os.path.join(app.instance_path, 'dd_monitor.db'),
        ),
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
    def index():
        return render_template('index.html')
        # return redirect(url_for('monitor.play'))

    # blueprint
    from app.blueprint import monitor
    from app.blueprint import dashboard
    app.register_blueprint(monitor.bp)
    app.register_blueprint(dashboard.bp)

    # blueprint - restful
    from app.api import rest
    from app.api import player_api
    from app.api import link_api
    from app.api import vue_api
    app.register_blueprint(rest)
    app.register_blueprint(link_api.bp)
    app.register_blueprint(player_api.bp)
    app.register_blueprint(vue_api.bp)

    return app
