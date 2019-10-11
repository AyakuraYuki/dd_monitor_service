# -*- coding: utf-8 -*-

from ..database import session as db_session
from ..model import Channel


def channels(query=''):
    return Channel.query.filter(Channel.name.like('%{}%'.format(query))).all()


def get_channel(cid=0):
    return Channel.query.filter(Channel.cid == cid).first()


def save(channel: Channel = None):
    db_session.add(channel)
    db_session.commit()


def delete(cid=0):
    db_session.delete(get_channel(cid))
    db_session.commit()
