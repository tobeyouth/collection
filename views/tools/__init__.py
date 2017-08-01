# -*- coding: utf-8 -*-

import json
import decimal

from flask.ext.restful import Api
from flask import make_response


def init_urls(app, urls):
    api = Api(app)
    for k, v in urls.iteritems():
        if isinstance(v, list):
            _v = [i for i in v]
            api.add_resource(k, *_v)
        else:
            api.add_resource(k, v)

    api.representations.update({
        'application/json': custom_json_output
    })


class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, decimal.Decimal):
            return str(obj)
        return json.JSONEncoder.default(self, obj)


def custom_json_output(data, code, headers=None):
    """ http://www.wiredmonk.me/customizing-flask-restful.html """
    dumped = json.dumps(data, cls=CustomEncoder)
    resp = make_response(dumped, code)
    resp.headers.extend(headers or {})
    return resp
