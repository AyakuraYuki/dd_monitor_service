import sqlite3
import click
from flask import current_app
from flask import g
from flask.cli import with_appcontext


def get_database():
    if 'application_database' not in g:
        g.application_database = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.application_database.row_factory = sqlite3.Row
    return g.application_database


def close_database(exception=None):
    database = g.pop('application_database', None)
    if database is not None:
        database.close()


def __init_schemas():
    database = get_database()
    with current_app.open_resource('schema.sql') as script:
        database.executescript(script.read().decode('utf8'))
    database.commit()
    database.close()


@click.command('init-schemas')
@with_appcontext
def init_schemas_command():
    __init_schemas()
    click.echo('Initialized database schemas.')


def init_app(app):
    app.teardown_appcontext(close_database)
    app.cli.add_command(init_schemas_command)
