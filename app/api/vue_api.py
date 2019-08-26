# -*- coding: utf-8 -*-

from flask import Blueprint, current_app

bp = Blueprint('api.vue', __name__)


@bp.route('/service-worker.js', methods=['GET'])
def service_worker():
    return current_app.send_static_file('service-worker.js')


@bp.route('/manifest.json', methods=['GET'])
def manifest():
    return current_app.send_static_file('manifest.json')


@bp.route('/robots.txt', methods=['GET'])
def robots():
    return current_app.send_static_file('robots.txt')


@bp.route('/favicon.ico', methods=['GET'])
def favicon():
    return current_app.send_static_file('favicon.ico')


@bp.route('/img/icons/<string:file>', methods=['GET'])
def img_icons(file):
    return current_app.send_static_file('img/icons/{}'.format(file))
