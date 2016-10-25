#!/bin/bash

export GAE_DEV=1
cd api_service
/home/py3env/bin/gunicorn --reload -b:8085 main:app &
cd ..
cd ae_service
/home/py3env/bin/gunicorn --reload -b:8090 main:app &
cd ..
