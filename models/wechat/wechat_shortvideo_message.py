# -*- coding: utf-8 -*-

from .wechat_message import WechatMessage
from .const import WECHAT_SHORTVIDEO_TYPE


class WechatShortVideoMessage(WechatMessage):

    message_type = WECHAT_SHORTVIDEO_TYPE
    media_id = ''
    thumb_media_id = ''
