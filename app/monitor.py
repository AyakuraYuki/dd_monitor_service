# -*- coding: utf-8 -*-

from flask import (
    Blueprint, render_template
)

from app import service

bp = Blueprint('monitor', __name__, url_prefix='/monitor')


@bp.route('/play')
def play():
    links = service.links()
    count = len(links)

    if count % 4 == 0:
        row_number = int(count / 4)
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
    for link in links:
        rows[row_index].append(link.link)
        index += 1
        if index == item_number:
            index = 0
            row_index += 1

    return render_template('player.html', rows=rows)
