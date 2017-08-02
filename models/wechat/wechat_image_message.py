# -*- coding: utf-8 -*-

from .wechat_message import WechatMessage
from .const import WECHAT_IMAGE_TYPE


class WechatImageMessage(WechatMessage):

    message_type = WECHAT_IMAGE_TYPE
    image = ''
    media_id = ''