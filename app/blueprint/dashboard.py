# -*- coding: utf-8 -*-

from flask import Blueprint, redirect, render_template, request, url_for, jsonify

from app import const
from app.bridge import link_bridge
from app.model import Link, to_json

bp = Blueprint('dashboard', __name__, url_prefix='/dashboard')


@bp.route('/language/<string:lang>')
def language(lang=''):
    if lang:
        const.language = lang
    return redirect(url_for('dashboard.dashboard'))


@bp.route('/index')
def dashboard():
    links = link_bridge.links()
    return render_template('dashboard.html', links=links, lang=const.current_lang_literal())


@bp.route('/save', methods=['POST'])
def save_link():
    form = request.form
    _id = int(form.get('_id'))
    title = form.get('title')
    link = form.get('link')
    sort = int(form.get('sort'))
    if _id == 0:
        link_bridge.insert(Link(_id=0, title=title, link=link, sort=link_bridge.latest_sort()))
    else:
        link_bridge.update(Link(_id=_id, title=title, link=link, sort=sort))
    return redirect(url_for('dashboard.dashboard'))


@bp.route('/save_channel_id', methods=['POST'])
def save_by_channel():
    form = request.form
    title = form.get('title')
    channel_id = form.get('channel')
    channel_id = str(channel_id).replace('https://www.youtube.com/channel/', '')
    link = f"https://www.youtube.com/embed/live_stream?channel={channel_id}"
    link_bridge.insert(Link(_id=0, title=title, link=link, sort=link_bridge.latest_sort()))
    return redirect(url_for('dashboard.dashboard'))


@bp.route('/link/<int:link_id>', methods=['GET'])
def get_link(link_id=0):
    link = link_bridge.get_link(link_id)
    return jsonify({'link': to_json(link)})


@bp.route('/link/<int:link_id>', methods=['DELETE'])
def delete_link(link_id=0):
    link_bridge.delete(link_id)
    links = link_bridge.links()
    return jsonify({'list': to_json(links)})
