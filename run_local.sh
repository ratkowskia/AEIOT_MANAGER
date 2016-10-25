#!/bin/bash

export GAE_DEV=1
/home/py3env/bin/gunicorn --reload -b:8080 mysite.wsgi &
cd api_service
/home/py3env/bin/gunicorn --reload -b:8085 main:app &
cd ..
cd ae_service
/home/py3env/bin/gunicorn --reload -b:8090 main:app &
cd ..
