# -*- coding: utf-8 -*-

import leancloud


class User(leancloud.Object):

    open_id = ''
    unique_id = ''
    avatar = ''
    name = ''