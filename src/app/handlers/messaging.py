import tornado.web
import os
import json
import firebase_admin
from firebase_admin import messaging
from firebase_admin.messaging import WebpushFCMOptions, WebpushConfig, FCMOptions
from caverimx.helpers import TemplateLoader, DB

template_loader = TemplateLoader('/recursos/vistas')

db = DB().get_database()
default_app = firebase_admin.initialize_app()


class SenderHandler(tornado.web.RequestHandler):
    def prepare(self):
        if self.request.headers.get('Content-Type') == 'application/json':
            self.request.body = json.loads(self.request.body)

    def put(self):
        topic = self.request.body.get('topic')
        msg_data = self.request.body.get('data')
        link = self.request.body.get('link')
        # See documentation on defining a message payload.
        message = messaging.Message(
            data=msg_data,
            topic=topic,
        )

        # Send a message to the devices subscribed to the provided topic.
        response = messaging.send(message)
        # Response is a message ID string.
        self.write(str(response))


class SubscribeHandler(tornado.web.RequestHandler):
    def prepare(self):
        if self.request.headers.get('Content-Type') == 'application/json':
            self.request.body = json.loads(self.request.body)

    def put(self):
        # subs = db.get_collection('subscriptions')
        token = self.request.body.get('token')
        topic = self.request.body.get('topic')
        self.write(str(messaging.subscribe_to_topic([token], topic)))

    def get(self):
        template = template_loader.get('landing/index.html')
        self.write(template.render(env=os.environ))
