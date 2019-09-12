# -*- coding: utf-8 -*-

from ..database import session
from ..model import Channel


def channels(query=''):
    return Channel.query.filter(Channel.name.like('%{}%'.format(query))).all()


def get_channel(cid=0):
    return Channel.query.filter(Channel.cid == cid).first()


def save(channel: Channel = None):
    session.add(channel)
    session.commit()


def delete(cid=0):
    session.delete(get_channel(cid))
    session.commit()
