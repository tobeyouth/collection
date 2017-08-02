# -*- coding: utf-8 -*-

from .wechat_message import WechatMessage
from .const import WECHAT_LOCATION_TYPE


class WechatLocationMessage(WechatMessage):

    message_type = WECHAT_LOCATION_TYPE
    location_x = ''
    location_y = ''
    scale = ''
    label = ''
