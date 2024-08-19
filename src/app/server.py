#!/usr/bin/env python
#
# Copyright 2009 Facebook
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import asyncio
import os
import handlers.websocket
import logging
from jinja2 import Template
from tornado.options import define, options
import router
from caverimx.helpers import TemplateLoader

define("port", default=4311, help="run on the given port", type=int)

async def main():
    tornado.options.parse_command_line()
    
    application: tornado.web.Application = tornado.web.Application(router.routes, **router.settings)
    application.listen(port=options.port)
    print("Server running on port {}".format(options.port))
    logging.info("Server running on port {}".format(options.port))
    await asyncio.Event().wait()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        tornado.ioloop.IOLoop.current().stop()
