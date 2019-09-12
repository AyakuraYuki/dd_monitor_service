# -*- coding: utf-8 -*-

from sqlite3 import IntegrityError

from flask import request, jsonify
from flask_restful import Resource

from ..bridge import channel_bridge
from ..model import Channel, to_json


class ChannelsApi(Resource):
    """
    :uri
        /_/channel
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
        channel_list = channel_bridge.channels(query)
        return jsonify({
            'list': to_json(channel_list)
        })

    @staticmethod
    def post():
        """
        :param
            name: YouTube channel name
            channelId: YouTube channel ID
        """
        data = request.json
        name = data.get('name')
        channel_id = data.get('channelId')
        channel = Channel(name=name, channel=channel_id)
        try:
            channel_bridge.save(channel)
        except IntegrityError:
            return jsonify({
                'status': -1,
                'message': "You're trying to add a channel which is existed, I am not allowing you to do this.",
                'data': {}
            })
        return jsonify({
            'channel': to_json(channel)
        })


class ChannelApi(Resource):
    """
    :uri
        /_/channel/cid/<int:cid>

    :param
        cid: <int> Channel ID
    """

    @staticmethod
    def get(cid):
        """
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

    @staticmethod
    def put(cid):
        """
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
        channel = Channel(cid=cid, name=name, channel=channel_id)
        channel_bridge.save(channel)
        return jsonify({
            'channel': to_json(channel_bridge.get_channel(cid))
        })

    @staticmethod
    def delete(cid):
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
        result = channel_bridge.delete(cid)
        return jsonify({
            'status': 0,
            'message': "done",
            'data': {
                'effect': result
            }
        })
