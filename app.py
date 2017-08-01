# -*- coding: utf-8 -*-

import sys


reload(sys)
sys.setdefaultencoding('utf-8')

from flask import Flask
from libs.middlewares import RequestMiddleware
from views import init_web


def create_app():
    app = Flask(__name__, template_folder='templates')
    init_web(app)
    app.wsgi_app = RequestMiddleware(app.wsgi_app)
    return app


app = create_app()
