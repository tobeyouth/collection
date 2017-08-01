# -*- coding: utf-8 -*-

from flask import request


class ApiError(Exception):

    # common
    bad_request = (999, '错误的请求', 400)
    not_found = (1000, '找不到对象', 404)
    permission_denied = (1001, '没有权限', 403)

    # priviledge
    need_login = (1014, '需要登录', 401)
    need_owner = (1013, '需要其拥有者', 403)

    # paras error
    bad_time_format = (1022, '无法识别的时间格式', 400)
    invalid_paras = (1026, '无效的参数', 400)
    not_enough_paras = (1027, '参数不足', 400)
    paras_validation_error = (1036, '参数不符合规范', 400)
    with_censor_ban_keyword = (1037, '内容含有当地法律的违禁内容', 400)

    # validate error
    invalid_item_id = (1040, '无效的item_id', 400)
    invalid_refund_apply = (1041, '无效的退款退货申请', 400)

    def __init__(self, error_msg, extra_msg=None):
        Exception.__init__(self)
        error_code, msg, status_code = error_msg
        is_api = request and request.path.startswith("/api/")
        self.code = status_code if is_api else 200
        self.msg = "%s (%s)" % (msg, extra_msg) if extra_msg else msg
        self.data = {
            'r': 1,
            'error': {
                'code': error_code,
                'message': self.msg,
            }
        }

    def __str__(self):
        return repr("%s %s" % (self.code, self.message))
