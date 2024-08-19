import handlers.websocket
import tornado.web
import handlers.websocket
import handlers.home
import handlers.messaging
settings = {
    'static_path': '/recursos/public',
}

routes = [
    (r"/messaging/send", handlers.messaging.SenderHandler),
    (r"/messaging/sub", handlers.messaging.SubscribeHandler),
    (r"/websocket", handlers.websocket.WebSocket),
    (r"/api", handlers.home.MainHandler),
    (r"/static/(.*)", tornado.web.StaticFileHandler,
     dict(path=settings['static_path'])),
]
