# -*- coding: utf-8 -*-


def to_json(obj):
    if obj is None:
        return {}
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
        if d is None:
            return None
        return Link(_id=d['_id'], title=d['title'], link=d['link'], sort=d['sort'])

    @staticmethod
    def orm(cursor_row):
        return Link(_id=cursor_row['id'], title=cursor_row['title'], link=cursor_row['link'], sort=cursor_row['sort'])
