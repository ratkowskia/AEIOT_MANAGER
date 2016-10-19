# Copyright 2015 Google Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")




#application = Flask(__name__)

#@application.route('/flask')
#def helloworld():
#    return 'Hello, World! from flask'

#@application.route('/')
#def run_django():
    #global application
#    return get_wsgi_application()

#if __name__ == '__main__':
#    # This is used when running locally. Gunicorn is used to run the
#    # application on Google App Engine. See entrypoint in app.yaml.
#    application.run(host='127.0.0.1', port=8080, debug=True)

application = get_wsgi_application()


