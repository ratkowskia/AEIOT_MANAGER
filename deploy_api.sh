#!/bin/bash

time gcloud -q app deploy  api_service/app.yaml --version dev
