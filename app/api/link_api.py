# -*- coding: utf-8 -*-

from flask import Blueprint, request, jsonify
from flask_restful import Resource

from ..bridge import link_bridge
from ..model import Link, to_json

bp = Blueprint('api.link', __name__, url_prefix='/_/link')


class LinksApi(Resource):
    """
    :uri
        /_/link
    """

    @staticmethod
    def get():
        """
        :param
            query: the keyword for fuzzy search, optional required while using the POST method
        """
        args = request.args
        if 'query' in args:
            query = args.get('query')
        else:
            query = ''
        link_list = link_bridge.links(query)
        return jsonify({
            'list': to_json(link_list)
        })

    @staticmethod
    def post():
        """
        :param
            title: link title or description
            link: link url
        """
        data = request.json
        title = data.get('title')
        url = data.get('link')
        link = Link(_id=0, title=title, link=url, sort=link_bridge.latest_sort())
        link_bridge.insert(link)
        return jsonify({
            'link': to_json(link)
        })


class LinkApi(Resource):
    """
    :uri
        /_/link/lid/<int:link_id>

    :param
        link_id: <int> Link ID
    """

    @staticmethod
    def get(link_id):
        """
        :return:
            {
                "link": {
                    "_id": 1,
                    "title": "title",
                    "link": "link",
                    "sort": 1
                }
            }
        """
        link = link_bridge.get_link(link_id)
        return jsonify({
            'link': to_json(link)
        })

    @staticmethod
    def put(link_id):
        """
        :param
            title: link title or description
            link: link url
            sort: the number of order

        :return:
            {
                "link": {
                    "_id": 1,
                    "title": "title",
                    "link": "link",
                    "sort": 1
                }
            }
        """
        data = request.json
        title = data.get('title')
        url = data.get('link')
        sort = int(data.get('sort'))
        link = Link(_id=link_id, title=title, link=url, sort=sort)
        link_bridge.update(link)
        return jsonify({
            'link': to_json(link)
        })

    @staticmethod
    def delete(link_id):
        """
        :return:
            {
                "status": 0,
                "message": "done",
                "data": {
                    "effect": 1
                }
            }
        """
        result = link_bridge.delete(link_id)
        return jsonify({
            'status': 0,
            'message': "done",
            'data': {
                'effect': result
            }
        })


@bp.route('/save/channel', methods=['POST'])
def save_by_channel():
    """
    :uri
        /_/link/save/channel

    :method
        POST

    :param
        title: link title or description
        channel: YouTube channel ID, allowed full channel url

    :return:
        {
            "link": {
                "_id": 1,
                "title": "title",
                "link": "link",
                "sort": 1
            }
        }
    """
    data = request.json
    title = data.get('title')
    channel_id = data.get('channel')
    channel_id = str(channel_id).replace('https://www.youtube.com/channel/', '')
    url = f"https://www.youtube.com/embed/live_stream?channel={channel_id}"
    link = Link(_id=0, title=title, link=url, sort=link_bridge.latest_sort())
    link_bridge.insert(link)
    return jsonify({
        'link': to_json(link)
    })
