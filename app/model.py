# -*- coding: utf-8 -*-

from sqlalchemy import Column, String, Integer

from .database import Base, session


def to_json(obj):
    """
    Convert object (or a collection of objects) to dict for json serialization.

    The object should have json() function.

    :param obj: One object or a collection of objects
    :return: A serializable dict
    """
    if obj is None:
        return {}
    if type(obj) is list:
        result = []
        for item in obj:
            result.append(item.json())
        return result
    return obj.json()


def when_import():
    pass


class Link(Base):
    __tablename__ = 'table_link'
    query = session.query_property()
    lid = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    link = Column(String)
    sort = Column(Integer)

    def json(self):
        return {
            '_id': self.lid,
            'title': self.title,
            'link': self.link,
            'sort': self.sort
        }

    def __repr__(self):
        return self.json()


class Channel(Base):
    __tablename__ = 'table_channel'
    query = session.query_property()
    cid = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    channel = Column(String)

    def json(self):
        return {
            '_id': self.cid,
            'name': self.name,
            'channel': self.channel
        }

    def __repr__(self):
        return self.json()
