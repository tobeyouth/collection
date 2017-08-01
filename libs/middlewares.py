# -*- coding:utf-8 -*-

from functools import wraps
from flask import request, g
from flask_restful import Resource


def is_weixin(request):
    wx_ua = 'micromessenger'
    ua = request.environ.get('HTTP_USER_AGENT', '')
    return wx_ua in ua.lower()


def is_mobile(request):
    mobile_ua = 'mobile'
    ua = request.environ.get('HTTP_USER_AGENT', '')
    return mobile_ua in ua.lower()


def insert_args(f):
    @wraps(f)
    def _(*args, **kwargs):
        args = list(args)
        request.is_weixin = is_weixin(request)
        request.is_mobile = is_mobile(request)
        g.scheme = request.environ['wsgi.url_scheme']
        args.insert(1, request)
        return f(*args, **kwargs)

    return _

class RequestMiddleware(object):

    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        ctx = self.app.im_self.request_context(environ)
        environ['is_weixin'] = is_weixin(ctx.request)
        environ['is_mobile'] = is_mobile(ctx.request)
        return self.app(environ, start_response)

class ApiResource(Resource):

    @insert_args
    def dispatch_request(self, *args, **kwargs):
        return super(ApiResource, self).dispatch_request(*args, **kwargs)
