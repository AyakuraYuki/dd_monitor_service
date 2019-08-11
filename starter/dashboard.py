import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from starter.database import get_database
from starter.model import Link
from starter import service

bp = Blueprint('dashboard', __name__, url_prefix='/_')


@bp.route('/index')
def dashboard():
    links = service.links()
    return render_template('dashboard.html', links=links)


@bp.route('/create', methods=['POST'])
def create_link():
    form = request.form
    title = form.get('title')
    link = form.get('link')
    service.insert(Link(_id=0, title=title, link=link))
    return redirect(url_for('dashboard.dashboard'))


@bp.route('/<int:link_id>/delete', methods=['GET'])
def delete_link(link_id=0):
    service.delete(link_id)
    return redirect(url_for('dashboard.dashboard'))
