# -*- coding:utf-8 -*-

from flask import request
from flask_restful.reqparse import Argument, RequestParser
from .error import ApiError


class MyArgument(Argument):

    def handle_validation_error(self, error):
        if isinstance(error, ApiError):
            raise error
        msg = self.help if self.help is not None else str(error)
        raise ApiError(ApiError.paras_validation_error, extra_msg=msg)


class RequestParser(RequestParser):

    def __init__(self, *args, **keywords):
        super(RequestParser, self).__init__(*args, **keywords)
        self.argument_class = MyArgument

    def parse_args(self, req=None, strict=None):
        if req is None:
            req = request
        namespace = self.namespace_class()

        req.unparsed_arguments = dict(self.argument_class('').source(req)) if strict else {}
        for arg in self.args:
            try:
                value, found = arg.parse(req)
                if found or arg.store_missing:
                    namespace[arg.dest or arg.name] = value
            except ApiError as e:
                er = e.data['error']
                er['message'] = '`%s` is incorrect. ' % arg.name + er['message']
                raise e

        return namespace
