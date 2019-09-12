# -*- coding: utf-8 -*-
from flask import Blueprint
from flask_restful import Api

from .channel_api import ChannelsApi, ChannelApi
from .link_api import LinksApi, LinkApi

rest = Blueprint('rest', __name__)

api = Api(rest)

api.add_resource(LinksApi, '/_/link')
api.add_resource(LinkApi, '/_/link/lid/<int:link_id>')

api.add_resource(ChannelsApi, '/_/channel')
api.add_resource(ChannelApi, '/_/channel/cid/<int:cid>')
