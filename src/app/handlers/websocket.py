import tornado.web
import tornado.websocket
class WebSocket(tornado.websocket.WebSocketHandler):
    def open(self):
        print("WebSocket opened")
        
    def check_origin(self, origin):
        return True

    def on_message(self, message):
        self.write_message(u"You said: " + message)

    def on_close(self):
        print("WebSocket closed")
