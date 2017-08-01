# -*- coding: utf-8 -*-

import os
import leancloud

from app import app
from cloud import engine


APP_ID = os.environ['LEANCLOUD_APP_ID']
APP_KEY = os.environ['LEANCLOUD_APP_KEY']
MASTER_KEY = os.environ['LEANCLOUD_APP_MASTER_KEY']
PORT = os.environ['LEANCLOUD_APP_PORT']

leancloud.init(APP_ID, app_key=APP_KEY, master_key=MASTER_KEY)
leancloud.use_master_key(False)

application = engine


if __name__ == '__main__':
    # local dev
    from gevent.pywsgi import WSGIServer
    from geventwebsocket.handler import WebSocketHandler
    from werkzeug.serving import run_with_reloader
    # from werkzeug.debug import DebuggedApplication

    @run_with_reloader
    def run():
        global application
        app.debug = True
        # application = DebuggedApplication(application, evalex=True)
        server = WSGIServer(('localhost', 3000), application, handler_class=WebSocketHandler)
        server.serve_forever()
    run()
