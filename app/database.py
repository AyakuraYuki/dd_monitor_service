# -*- coding: utf-8 -*-

import sqlite3

import click
from DBUtils.PooledDB import PooledDB
from flask import current_app
from flask import g
from flask.cli import with_appcontext

from app.const import Singleton


class SQLiteCP(metaclass=Singleton):
    __pool = None

    def connection(self):
        if self.__pool is None:
            self.__pool = PooledDB(
                creator=sqlite3,
                mincached=10,
                maxcached=50,
                maxshared=20,
                maxconnections=100,
                blocking=True,
                maxusage=0,
                database=current_app.config['DATABASE']
            )
        return self.__pool.connection()


def get_database():
    if 'application_database' not in g:
        g.application_database = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.application_database.row_factory = sqlite3.Row
    return g.application_database


def execute_update(sql='', parameters=None):
    if sql == '' or ('?' in sql and parameters is None):
        return 0
    with get_database() as db:
        cursor = db.cursor().execute(sql, parameters)
        row_count = cursor.rowcount
        db.commit()
    return row_count


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
