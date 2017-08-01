# -*- coding: utf-8 -*

import os

from flask import abort
from libs.middlewares import ApiResource
from libs.decorators import arguments, convert_data
from wechatpy.utils import check_signature
from wechatpy import parse_message, create_reply
from wechatpy.exceptions import (
    InvalidSignatureException,
    InvalidAppIdException,
)


WECHAT_TOKEN = os.environ['WECHAT_TOKEN']
WECHAT_APP_ID = os.environ['WECHAT_APP_ID']
WECHAT_APP_SECRET = os.environ['WECHAT_APP_SECRET']
WECHAT_AES_KEY = os.environ['WECHAT_AES_KEY']


class ChatApi(ApiResource):

    @convert_data
    @arguments({
        'signature': {'type': str},
        'timestamp': {'type': str},
        'nonce': {'type': str},
        'encrypt_type': {'type': str, 'default': 'raw'},
        'msg_signature': {'type': str}
    })
    def post(self, request):
        signature = request.req_args.get('signature', '')
        timestamp = request.req_args.get('timestamp', '')
        nonce = request.req_args.get('nonce', '')
        encrypt_type = request.req_args.get('encrypt_type', 'raw')
        msg_signature = request.req_args.get('msg_signature', '')


        try:
            check_signature(WECHAT_TOKEN, signature, timestamp, nonce)
        except InvalidSignatureException as e:
            print e
            abort(403)

        # plaintext mode
        if encrypt_type == 'raw':
            if msg.type == 'text':
                reply = create_reply(msg.content, msg)
            else:
                reply = create_reply('Hi!', msg)
            return reply.render()
        else:
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
                if msg.type == 'text':
                    reply = create_reply(msg.content, msg)
                else:
                    reply = create_reply('Sorry, can not handle this for now', msg)
                return crypto.encrypt_message(reply.render(), nonce, timestamp)

