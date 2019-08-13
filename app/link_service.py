# -*- coding: utf-8 -*-

from app.database import get_database
from app.model import Link


def links(query=''):
    result = []
    sql = "SELECT * FROM table_link WHERE title LIKE '%' || ? || '%' ORDER BY sort"
    parameters = (query,)

    with get_database() as db:
        cursor = db.cursor().execute(sql, parameters)
        for row in cursor:
            link = Link.orm(row)
            result.append(link)

    return result


def get_link(_id=0):
    if _id == 0:
        return None
    sql = "SELECT * FROM table_link WHERE id = ?"
    parameters = (_id,)

    with get_database() as db:
        cursor = db.cursor().execute(sql, parameters)
        row = cursor.fetchone()
        if row is not None:
            link = Link.orm(row)
        else:
            link = None

    return link


def __update(sql='', parameters=None):
    if sql == '' or ('?' in sql and parameters is None):
        return 0
    with get_database() as db:
        cursor = db.cursor().execute(sql, parameters)
        row_count = cursor.rowcount
        db.commit()
    return row_count


def insert(link: Link = None):
    if link is None:
        return 0
    sql = "INSERT INTO table_link (title, link, sort) VALUES (?, ?, ?)"
    parameters = (link.title, link.link, link.sort,)
    return __update(sql, parameters)


def update(link: Link = None):
    if link is None:
        return 0
    sql = "UPDATE table_link SET title = ?, link = ?, sort = ? WHERE id = ?"
    parameters = (link.title, link.link, link.sort, link.id(),)
    return __update(sql, parameters)


def delete(_id=0):
    if _id == 0:
        return 0
    sql = "DELETE FROM table_link WHERE id = ?"
    parameters = (_id,)
    return __update(sql, parameters)


def latest_sort():
    sql = "SELECT count(*) + 1 AS 'count' FROM table_link"
    with get_database() as db:
        cursor = db.cursor().execute(sql)
        count = cursor.fetchone()['count']
    return count
