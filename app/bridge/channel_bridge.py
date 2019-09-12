# -*- coding: utf-8 -*-

from ..database import get_database, execute_update
from ..model import Channel


def channels(query=''):
    result = []
    sql = "SELECT * FROM table_channel WHERE name LIKE '%' || ? || '%' ORDER BY name"
    parameters = (query,)

    with get_database() as db:
        cursor = db.cursor().execute(sql, parameters)
        for row in cursor:
            channel = Channel.orm(row)
            result.append(channel)

    return result


def get_channel(_id=0):
    if _id == 0:
        return None
    sql = "SELECT * FROM table_channel WHERE id = ?"
    parameters = (_id,)

    with get_database() as db:
        cursor = db.cursor().execute(sql, parameters)
        row = cursor.fetchone()
        if row is not None:
            channel = Channel.orm(row)
        else:
            channel = None

    return channel


def insert(channel: Channel = None):
    if channel:
        sql = "INSERT INTO table_channel (name, channel) VALUES (?, ?)"
        parameters = (channel.name, channel.channel,)
        return execute_update(sql, parameters)
    else:
        return 0


def update(channel: Channel = None):
    if channel:
        sql = "UPDATE table_channel SET name = ?, channel = ? WHERE id = ?"
        parameters = (channel.name, channel.channel, channel.id(),)
        return execute_update(sql, parameters)
    else:
        return 0


def delete(_id=0):
    if _id:
        sql = "DELETE FROM table_channel WHERE id = ?"
        parameters = (_id,)
        return execute_update(sql, parameters)
    else:
        return 0
