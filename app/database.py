# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine('sqlite:///instance/dd_monitor.db', convert_unicode=True)
session = scoped_session(sessionmaker(bind=engine))
Base = declarative_base()


def init_db():
    from . import model
    Base.metadata.create_all(bind=engine)
    model.when_import()


def shutdown(exception=None):
    session.remove()


def init_app(app):
    init_db()
    app.teardown_appcontext(shutdown)
