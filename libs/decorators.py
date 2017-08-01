# -*- coding: utf-8 -*-

from flask import request
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
