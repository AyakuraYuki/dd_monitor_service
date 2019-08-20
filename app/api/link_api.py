# -*- coding: utf-8 -*-

from flask import Blueprint, request, jsonify

from app.bridge import link_bridge
from app.model import Link, to_json

bp = Blueprint('api.link', __name__, url_prefix='/_/link')


@bp.route('/list', methods=['GET', 'POST'])
def links():
    """
    :uri
        /_/link/list

    :method
        GET
        POST

    :param
        query: the keyword for fuzzy search, optional required while using the POST method

    :return:
        {
            "list": [
                {
                    "_id": 1,
                    "title": "title",
                    "link": "link",
                    "sort": 1
                }
            ]
        }
    """
    method = request.method
    if method == 'POST':
        form = request.form
        query = form.get('query')
    else:
        query = ''
    link_list = link_bridge.links(query)
    return jsonify({
        'list': to_json(link_list)
    })


@bp.route('/save', methods=['POST'])
def save():
    """
    :uri
        /_/link/save

    :method
        POST

    :param
        title: link title or description
        link: link url

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
    link = Link(_id=0, title=title, link=url, sort=link_bridge.latest_sort())
    link_bridge.insert(link)
    return jsonify({
        'link': to_json(link)
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
    form = request.form
    title = form.get('title')
    channel_id = form.get('channel')
    channel_id = str(channel_id).replace('https://www.youtube.com/channel/', '')
    url = f"https://www.youtube.com/embed/live_stream?channel={channel_id}"
    link = Link(_id=0, title=title, link=url, sort=link_bridge.latest_sort())
    link_bridge.insert(link)
    return jsonify({
        'link': to_json(link)
    })


@bp.route('/lid/<int:link_id>', methods=['PUT'])
def update(link_id):
    """
    :uri
        /_/link/lid/<link_id>

    :method
        PUT

    :param
        link_id: <int> Link ID
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
    if link_id:
        data = request.json
        title = data.get('title')
        url = data.get('link')
        sort = int(data.get('sort'))
        link = Link(_id=link_id, title=title, link=url, sort=sort)
        link_bridge.update(link)
        return jsonify({
            'link': to_json(link)
        })
    else:
        return jsonify({
            'link': None
        })


@bp.route('/lid/<int:link_id>', methods=['GET'])
def get(link_id):
    """
    :uri
        /_/link/lid/<link_id>

    :method
        GET

    :param
        link_id: <int> Link ID

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


@bp.route('/lid/<int:link_id>', methods=['DELETE'])
def delete(link_id):
    """
    :uri
        /_/link/lid/<link_id>

    :method
        DELETE

    :param
        link_id: <int> Link ID

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
