# -*- coding: utf-8 -*-

WECHAT_TEXT_TYPE = 'text'
WECHAT_IMAGE_TYPE = 'image'
WECHAT_VOICE_TYPE = 'voice'
WECHAT_VIDEO_TYPE = 'video'
WECHAT_SHORTVIDEO_TYPE = 'shortvideo'
WECHAT_LOCATION_TYPE = 'location'
WECHAT_LINK_TYPE = 'link'

WECHAT_MESSAGE_TYPES = (
    WECHAT_TEXT_TYPE,
    WECHAT_IMAGE_TYPE,
    WECHAT_VOICE_TYPE,
    WECHAT_VIDEO_TYPE,
    WECHAT_SHORTVIDEO_TYPE,
    WECHAT_LOCATION_TYPE,
    WECHAT_LINK_TYPE
)

WECHAT_EVENT_TYPE = 'event'

WECHAT_EVENT_SUBSCRIBE = 'subscribe'
WECHAT_EVENT_UNSUBSCRIBE = 'unsubscribe'
WECHAT_EVENT_LOCATION = 'LOCATION'
WECHAT_EVENT_CLICK = 'CLICK'
WECHAT_EVENT_SCAN = 'SCAN'


WECHAT_EVENTS = (
    WECHAT_EVENT_SUBSCRIBE,
    WECHAT_EVENT_UNSUBSCRIBE,
    WECHAT_EVENT_LOCATION,
    WECHAT_EVENT_CLICK,
    WECHAT_EVENT_SCAN
)