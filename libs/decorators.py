# -*- coding: utf-8 -*-

import json
from flask import request, make_response
from .reqparse import RequestParser
from functools import wraps


def arguments(schema):
    def decorator(f):
        @wraps(f)
        def _(*args, **kwargs):
            parser = RequestParser()
            for field, config in schema.iteritems():
                parser.add_argument(field, **config)
            setattr(request, 'req_args', parser.parse_args())
            return f(*args, **kwargs)

        return _
    return decorator

def convert_data(func):
    @wraps(func)
    def _wrap(instance, request, *args, **kwargs):
        r = func(instance, request, *args, **kwargs)
        
        data_type = request.headers.get('Content-Type')
        
        if not data_type:
            data_type = 'text/html; charset=utf-8'
            # data_type = 'text/plain;'
        if 'xml' in data_type:
            response = make_response(r)
            response.headers['Content-Type'] = 'text/xml'
            return response
        else:
            response = make_response(r)
            response.headers['Content-Type'] = data_type
            return response

    return _wrap