# -*- coding: utf-8 -*-

from leancloud import HttpsRedirectMiddleware, Engine, LeanEngineError
from app import app


# app = HttpsRedirectMiddleware(app)
engine = Engine(app)


@engine.define
def hello(**params):
    if 'name' in params:
        return 'Hello, {}!'.format(params['name'])
    else:
        return 'Hello, LeanCloud!'
