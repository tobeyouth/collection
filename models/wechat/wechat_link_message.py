# -*- coding: utf-8 -*-

from .wechat_message import WechatMessage
from .const import WECHAT_LINK_TYPE


class WechatLinkMessage(WechatMessage):

    message_type = WECHAT_LINK_TYPE
    title = ''
    description = ''
    url = ''
