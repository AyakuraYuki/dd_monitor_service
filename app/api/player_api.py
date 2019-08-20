# -*- coding: utf-8 -*-

from flask import Blueprint, jsonify

from app.bridge import link_bridge
from app.model import to_json

bp = Blueprint('api.player', __name__, url_prefix='/player')


@bp.route('/list')
def player_list():
    """
    :uri
        /player/list

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
    link_list = link_bridge.links()
    return jsonify({
        'list': to_json(link_list)
    })
