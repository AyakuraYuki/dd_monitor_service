import os

from flask import Flask
from flask import url_for
from flask import redirect


def create_app(test_config=None):
    """
    Create a flask application.
    :param test_config: Test configuration
    :return: application instance
    """
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        DATABASE=os.path.join(app.instance_path, 'dd_monitor.db'),
        SECRET_KEY='dev' if app.debug else '2c830312-bb99-11e9-8018-6245b50a3dbc',
    )

    # load the instance config if it is exists, when not testing
    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # database
    from . import database
    database.init_app(app)

    # router mapping
    @app.route('/')
    def hello():
        return redirect(url_for('monitor.play'))

    # blueprint
    from . import monitor, dashboard
    app.register_blueprint(monitor.bp)
    app.register_blueprint(dashboard.bp)

    return app
