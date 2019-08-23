# -*- coding: utf-8 -*-

from flask import Blueprint, request, jsonify

from app.bridge import channel_bridge
from app.model import Channel, to_json

bp = Blueprint('api.channel', __name__, url_prefix='/_/channel')


@bp.route('/list', methods=['GET', 'POST'])
def channels():
    """
    :uri
        /_/channel/list

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
                    "name": "name",
                    "channel": "channel_id"
                }
            ]
        }
    """
    method = request.method
    if method == 'POST':
        data = request.json
        query = data.get('query')
    else:
        query = ''
    channel_list = channel_bridge.channels(query)
    return jsonify({
        'list': to_json(channel_list)
    })


@bp.route('/save', methods=['POST'])
def save():
    """
    :uri
        /_/channel/save

    :method
        POST

    :param
        name: YouTube channel name
        channelId: YouTube channel ID

    :return:
        {
            "channel": {
                "_id": 1,
                "name": "name",
                "channel": "channel_id"
            }
        }
    """
    data = request.json
    name = data.get('name')
    channel_id = data.get('channelId')
    channel = Channel(_id=0, name=name, channel=channel_id)
    channel_bridge.insert(channel)
    return jsonify({
        'channel': to_json(channel)
    })


@bp.route('/cid/<int:cid>', methods=['PUT'])
def update(cid):
    """
    :uri
        /_/channel/cid/<cid>

    :method
        PUT

    :param
        cid: <int> Channel ID
        name: YouTube channel name
        channelId: YouTube channel ID

    :return:
        {
            "channel": {
                "_id": 1,
                "name": "name",
                "channel": "channel_id"
            }
        }
    """
    if cid:
        data = request.json
        name = data.get('name')
        channel_id = data.get('channelId')
        channel = Channel(_id=cid, name=name, channel=channel_id)
        channel_bridge.update(channel)
        return jsonify({
            'channel': to_json(channel)
        })
    else:
        return jsonify({
            'channel': None
        })


@bp.route('/cid/<int:cid>', methods=['GET'])
def get(cid):
    """
    :uri
        /_/channel/cid/<cid>

    :method
        GET

    :param
        cid: <int> Channel ID

    :return:
        {
            "channel": {
                "_id": 1,
                "name": "name",
                "channel": "channel_id"
            }
        }
    """
    channel = channel_bridge.get_channel(cid)
    return jsonify({
        'channel': to_json(channel)
    })


@bp.route('/cid/<int:cid>', methods=['DELETE'])
def delete(cid):
    """
    :uri
        /_/channel/cid/<cid>

    :method
        DELETE

    :param
        cid: <int> Channel ID

    :return:
        {
            "status": 0,
            "message": "done",
            "data": {
                "effect": 1
            }
        }
    """
    result = channel_bridge.delete(cid)
    return jsonify({
        'status': 0,
        'message': "done",
        'data': {
            'effect': result
        }
    })
