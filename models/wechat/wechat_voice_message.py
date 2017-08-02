# -*- coding: utf-8 -*-

from .wechat_message import WechatMessage
from .const import WECHAT_VOICE_TYPE


class WechatVoiceMessage(WechatMessage):

    message_type = WECHAT_VOICE_TYPE
    media_id = ''
    format = ''
    recognition = ''
