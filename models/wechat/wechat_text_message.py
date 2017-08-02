# -*- coding: utf-8 -*-

from .wechat_message import WechatMessage
from .const import WECHAT_TEXT_TYPE


class WechatTextMessage(WechatMessage):

    message_type = WECHAT_TEXT_TYPE
    content = ''
