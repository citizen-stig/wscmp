from tornado import web, ioloop
from sockjs.tornado import SockJSRouter, SockJSConnection

from constants import HTTP_WS_PORT, HTTP_WS_URL


class EchoConnection(SockJSConnection):
    def on_message(self, msg):
        self.send(msg)

if __name__ == '__main__':
    EchoRouter = SockJSRouter(EchoConnection, HTTP_WS_URL)

    app = web.Application(EchoRouter.urls)
    app.listen(HTTP_WS_PORT)
    ioloop.IOLoop.instance().start()
