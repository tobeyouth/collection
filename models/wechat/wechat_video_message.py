# -*- coding: utf-8 -*-

from .wechat_message import WechatMessage
from .const import WECHAT_VIDEO_TYPE


class WechatVideoMessage(WechatMessage):

    message_type = WECHAT_VIDEO_TYPE
    media_id = ''
    thumb_media_id = ''
