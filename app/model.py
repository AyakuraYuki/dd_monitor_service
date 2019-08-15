# -*- coding: utf-8 -*-


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


class Link:
    def __init__(self, _id=0, title='', link='', sort=0):
        self._id = _id
        self.title = title
        self.link = link
        self.sort = sort

    def id(self):
        return self._id

    def __repr__(self):
        return f'Link [_id: {self._id}, title: "{self.title}", link: "{self.link}", sort: {self.sort}]'

    def json(self):
        return {
            '_id': self._id,
            'title': self.title,
            'link': self.link,
            'sort': self.sort
        }

    @staticmethod
    def dump(d):
        if d:
            return Link(_id=d['_id'], title=d['title'], link=d['link'], sort=d['sort'])
        else:
            return None

    @staticmethod
    def orm(cursor_row):
        return Link(_id=cursor_row['id'], title=cursor_row['title'], link=cursor_row['link'], sort=cursor_row['sort'])


class Channel:
    def __init__(self, _id=0, name='', channel=''):
        self._id = _id
        self.name = name
        self.channel = channel

    def id(self):
        return self._id

    def __repr__(self):
        return f'Channel [_id: {self._id}, name: {self.name}, channel: {self.channel}]'

    def json(self):
        return {
            '_id': self._id,
            'name': self.name,
            'channel': self.channel
        }

    @staticmethod
    def dump(d):
        if d:
            return Channel(_id=d['_id'], name=d['name'], channel=d['channel'])
        else:
            return None

    @staticmethod
    def orm(cursor_row):
        return Channel(_id=cursor_row['id'], name=cursor_row['name'], channel=cursor_row['channel'])
