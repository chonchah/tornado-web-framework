from jinja2 import Template
from os import getenv
import pymongo


class DB (pymongo.MongoClient):
    def __init__(self):
        super().__init__(host="mongodb://mongo/%s" % (getenv('MONGODB_DB')), port=27017, authSource=getenv('MONGODB_DB'), username=getenv(
            'MONGODB_USER'), password=getenv('MONGODB_PASSWD'))


class TemplateLoader:
    def __init__(self, path_dir):
        self.path_dir = path_dir

    def get(self, name):
        with open('%s/%s' % (self.path_dir, name)) as file:
            template = file.read()
            file.close()
            return Template(template)
