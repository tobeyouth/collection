# -*- coding: utf-8 -*-

# 处理不同类型的消息
# 消息分为:
# 1. 普通消息
# 2. 事件推送
# 调用 handler 后，可以调用 reply 方法返回消息

from models.wechat import message_save
from wechatpy import create_reply
from models.wechat.const import (WECHAT_EVENT_TYPE, WECHAT_MESSAGE_TYPES, 
                                 WECHAT_EVENTS, WECHAT_EVENT_SUBSCRIBE,
                                 WECHAT_EVENT_UNSUBSCRIBE, WECHAT_EVENT_LOCATION,
                                 WECHAT_EVENT_CLICK, WECHAT_EVENT_SCAN)



def common_message_handler(msg, encrypt_type):
    r, r_msg = message_save(msg, encrypt_type)
    if not r:
        reply = create_reply('出了点儿问题: %s' % r_msg, msg)
    else:
        reply = create_reply('%s 你的信息我已收到' % r_msg, msg)
    return reply

def event_handler(msg, encrypt_type):
    event = msg.event
    
    if event is None or event not in WECHAT_EVENTS:
        reply = create_reply('event: %s is incorrect' % event, msg)

    if event == WECHAT_EVENT_SUBSCRIBE:
        ticket = msg.get('ticket', None)
        if ticket is None:
            return subscribe_hander(msg)
        return subscribe_ticket_hander(msg)
    elif event == WECHAT_EVENT_SCAN:
        return scan_handler(msg)
    elif event == WECHAT_EVENT_LOCATION:
        return location_handler(msg)
    elif event == WECHAT_EVENT_CLICK(msg):
        return click_hander(msg)

# 关注
def subscribe_hander(msg):
    reply = create_reply('欢迎关注, 可以点击菜单栏中的[收藏夹]创建自己的收藏夹', msg)
    return reply

# 未关注时扫描场景二维码
def subscribe_ticket_hander(msg):
    pass

# 关注后扫描场景二维码
def scan_handler(msg):
    pass

# 上报地理位置
def location_handler(msg):
    pass

# 点击自定义菜单
def click_hander(msg):
    pass

def create_reply_from_handler(msg, encrypt_type):
    msg_type = msg.type

    if msg_type == WECHAT_EVENT_TYPE:
        return event_handler(msg, encrypt_type)
    elif msg_type in WECHAT_MESSAGE_TYPES:
        return common_message_handler(msg, encrypt_type)
    return create_reply('msg_type: %s is incorrect' % msg_type, msg)
    # return False, 'msg_type: %s is incorrect' % msg_type