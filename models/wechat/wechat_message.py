# -*- coding: utf-8 -*-

import leancloud


class WechatMessage(leancloud.Object):

    message_type = ''
    message_id = ''
    source = ''
    target = ''
    create_time = ''
    encrypt_type = ''

    def _save(self, data):
        self.set('message_type', self.message_type)
        for k, v in data.iteritems():
            self.set(k, v)
        self.save()
