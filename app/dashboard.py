# -*- coding: utf-8 -*-

from flask import Blueprint, redirect, render_template, request, url_for, jsonify

from app import link_service
from app.model import Link, to_json

bp = Blueprint('dashboard', __name__, url_prefix='/_')


@bp.route('/index')
def dashboard():
    links = link_service.links()
    return render_template('dashboard.html', links=links)


@bp.route('/save', methods=['POST'])
def save_link():
    form = request.form
    _id = int(form.get('_id'))
    title = form.get('title')
    link = form.get('link')
    sort = int(form.get('sort'))
    if _id == 0:
        link_service.insert(Link(_id=0, title=title, link=link, sort=link_service.latest_sort()))
    else:
        link_service.update(Link(_id=_id, title=title, link=link, sort=sort))
    return redirect(url_for('dashboard.dashboard'))


@bp.route('/save_channel_id', methods=['POST'])
def save_link_by_channel_id():
    form = request.form
    title = form.get('title')
    channel_id = form.get('channel')
    link = f"https://www.youtube.com/embed/live_stream?channel={channel_id}"
    link_service.insert(Link(_id=0, title=title, link=link, sort=link_service.latest_sort()))
    return redirect(url_for('dashboard.dashboard'))


@bp.route('/<int:link_id>/delete', methods=['GET'])
def delete_link(link_id=0):
    link_service.delete(link_id)
    return redirect(url_for('dashboard.dashboard'))


@bp.route('/get', methods=['POST'])
def get_link():
    form = request.form
    _id = form.get('id')
    link = link_service.get_link(_id)
    return jsonify(to_json(link))
