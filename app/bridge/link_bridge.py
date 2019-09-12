# -*- coding: utf-8 -*-

from ..database import session
from ..model import Link


def links(query=''):
    return Link.query.filter(Link.title.like('%{}%'.format(query))).all()


def get_link(lid=0):
    return Link.query.filter(Link.lid == lid).first()


def save(link: Link = None):
    if link:
        session.add(link)
        session.commit()


def update(link: Link = None):
    if link:
        modify = session.query(Link).filter(Link.lid == link.lid).scalar()
        modify.title = link.title
        modify.link = link.link
        modify.sort = link.sort
        session.commit()


def delete(lid=0):
    session.delete(get_link(lid))
    session.commit()


def latest_sort():
    return len(Link.query.all()) + 1
