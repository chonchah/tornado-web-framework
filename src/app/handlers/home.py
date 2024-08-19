import tornado.web, os
from caverimx.helpers import TemplateLoader

template_loader = TemplateLoader('/recursos/vistas')

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        template = template_loader.get('landing/index.html')
        self.write(template.render(env=os.environ))
