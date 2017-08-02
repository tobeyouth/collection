# -*- coding: utf-8 -*-

from .index import index
from flask import request
from libs.decorators import arguments, convert_data
from views.wechat import wechat_message_bp


def init_web(app):
    app.add_url_rule('/', 'index', index)
    app.register_blueprint(wechat_message_bp)

    for func in (map, sorted, sum, max, min, str, int, hasattr, enumerate, len):
        app.add_template_global(func)

    return app
