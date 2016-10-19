try:
    from routes import Mapper
except ImportError:
    print("This example requires Routes to be installed")

# Obviously you'd import your app callables
# from different places...
#from test import app as app1
#from test import app as app2

import os
from django.core.wsgi import get_wsgi_application
from flask import Flask

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
app_manager = get_wsgi_application()
app_hw = Flask(__name__)

class Application(object):
    def __init__(self):
        self.map = Mapper()
        self.map.connect('app_manager', '/', application=app_manager)
        self.map.connect('app_hw', '/hw', application=app_hw)

    def __call__(self, environ, start_response):
        match = self.map.routematch(environ=environ)
        if not match:
            return self.error404(environ, start_response)
        return match[0]['application'](environ, start_response)

    def error404(self, environ, start_response):
        html = b"""\
        <html>
          <head>
            <title>404 - Not Found</title>
          </head>
          <body>
            <h1>404 - Not Found</h1>
          </body>
        </html>
        """
        headers = [
            ('Content-Type', 'text/html'),
            ('Content-Length', str(len(html)))
        ]
        start_response('404 Not Found', headers)
        return [html]

application = Application()