# -*- coding: utf-8 -*-


class Link:
    def __init__(self, _id=0, title='', link='', sort=0):
        self._id = _id
        self.title = title
        self.link = link
        self.sort = sort

    def id(self):
        return self._id
