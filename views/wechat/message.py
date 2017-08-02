# -*- coding: utf-8 -*-

import os

from flask import abort, request, Blueprint
from wechatpy.utils import check_signature
from wechatpy import parse_message, create_reply
from wechatpy.crypto import WeChatCrypto
from wechatpy.exceptions import (
    InvalidSignatureException,
    InvalidAppIdException,
)
from views.wechat.handler import create_reply_from_handler
from models.wechat import message_save


WECHAT_TOKEN = os.environ['WECHAT_TOKEN']
WECHAT_APP_ID = os.environ['WECHAT_APP_ID']
WECHAT_APP_SECRET = os.environ['WECHAT_APP_SECRET']
WECHAT_AES_KEY = os.environ['WECHAT_AES_KEY']

wechat_message_bp = Blueprint('wechat_message_bp', __name__)

@wechat_message_bp.route('/wechat/message', methods=['GET', 'POST'])
def message():
    signature = request.args.get('signature', '')
    timestamp = request.args.get('timestamp', '')
    nonce = request.args.get('nonce', '')
    encrypt_type = request.args.get('encrypt_type', 'raw')
    msg_signature = request.args.get('msg_signature', '')
    
    try:
        check_signature(WECHAT_TOKEN, signature, timestamp, nonce)
    except InvalidSignatureException:
        abort(403)
    

    # check
    if request.method == 'GET':
        echo_str = request.args.get('echostr', '')
        return echo_str

    # message
    if encrypt_type == 'raw':
        # plaintext mode
        msg = parse_message(request.data)
        reply = create_reply_from_handler(msg, encrypt_type)
        return reply.render()
    else:
        # encryption mode
        from wechatpy.crypto import WeChatCrypto
        crypto = WeChatCrypto(WECHAT_TOKEN, WECHAT_AES_KEY, WECHAT_APP_ID)
        try:
            msg = crypto.decrypt_message(
                request.data,
                msg_signature,
                timestamp,
                nonce
            )
        except (InvalidSignatureException, InvalidAppIdException):
            abort(403)
        else:
            msg = parse_message(msg)
            reply = create_reply_from_handler(msg, encrypt_type)
            return crypto.encrypt_message(reply.render(), nonce, timestamp)