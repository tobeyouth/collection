# -*- coding: utf-8 -*

from .index import index
from .wechat import init_wechat_urls


def init_web(app):
    app.add_url_rule('/', 'index', index)

    init_wechat_urls(app)

    for func in (map, sorted, sum, max, min, str, int, hasattr, enumerate, len):
        app.add_template_global(func)

    return app
