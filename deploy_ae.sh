#!/bin/bash

time gcloud -q app deploy ae_service/app.yaml --version dev
