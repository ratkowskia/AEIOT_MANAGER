#!/bin/bash

time gcloud -q app deploy app.yaml api_service/app.yaml ae_service/app.yaml --version dev
