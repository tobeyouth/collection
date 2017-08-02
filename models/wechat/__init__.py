# -*- coding: utf-8 -*-

from .wechat_message import WechatMessage
from .wechat_text_message import WechatTextMessage
from .wechat_video_message import WechatVideoMessage
from .wechat_image_message import WechatImageMessage
from .wechat_voice_message import WechatVoiceMessage
from .wechat_shortvideo_message import WechatShortVideoMessage
from .wechat_location_message import WechatLocationMessage
from .wechat_link_message import WechatLinkMessage
from .const import (WECHAT_IMAGE_TYPE, WECHAT_LINK_TYPE, WECHAT_LOCATION_TYPE,
                    WECHAT_SHORTVIDEO_TYPE, WECHAT_TEXT_TYPE, WECHAT_VIDEO_TYPE,
                    WECHAT_VOICE_TYPE)



def message_save(msg, encrypt_type):
    message_type = msg.type
    message = None
    message_data = dict(message_id=msg.id,
                        source=msg.source,
                        target=msg.target,
                        create_time=msg.create_time,
                        encrypt_type=encrypt_type)
    if message_type == WECHAT_IMAGE_TYPE:
        message = WechatImageMessage()
        message_data['image'] = msg.image
        message_data['media_id'] = msg.media_id
    elif message_type == WECHAT_LINK_TYPE:
        message = WechatLinkMessage()
        message_data['title'] = msg.title
        message_data['description'] = msg.description
        message_data['url'] = msg.url
    elif message_type == WECHAT_LOCATION_TYPE:
        message = WechatLocationMessage
        message_data['location_x'] = msg.location_x
        message_data['location_y'] = msg.location_y
        message_data['scale'] = msg.sacle
        message_data['label'] = msg.label
        message_data['location'] = msg.location
    elif message_type == WECHAT_SHORTVIDEO_TYPE:
        message = WechatShortVideoMessage()
        message_data['media_id'] = msg.media_id
        message_data['thumb_media_id'] = msg.thumb_media_id
    elif message_type == WECHAT_TEXT_TYPE:
        message = WechatTextMessage()
        message_data['content'] = msg.content
    elif message_type == WECHAT_VIDEO_TYPE:
        message = WechatVideoMessage()
        message_data['media_id'] = msg.media_id
        message_data['thumb_media_id'] = msg.thumb_media_id
    elif message_type == WECHAT_VOICE_TYPE:
        message = WechatVoiceMessage()
        message_data['media_id'] = msg.media_id
        message_data['format'] = msg.format
        message_data['recognition'] = msg.recognition

    if message:
        print 'message_data'
        print message_data

        message._save(data=message_data)
        return True, 'save success'
    
    return False, 'message_type error'