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
    count = len(link_list)

    if count % 5 == 0:
        row_number = int(count / 5) + 1
        item_number = 5
    elif count % 4 == 0:
        row_number = int(count / 4) + 1
        item_number = 4
    elif count % 3 == 0:
        row_number = int(count / 3) + 1
        item_number = 3
    else:
        row_number = int(count / 2) + 1
        item_number = 2

    rows = []
    for i in range(row_number):
        rows.append([])
    index = 0
    row_index = 0
    for link in link_list:
        rows[row_index].append(link.link)
        index += 1
        if index == item_number:
            index = 0
            row_index += 1

    return jsonify({
        'playlist': rows
    })
