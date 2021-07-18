#!/bin/sh

# exit the script on any error
set -e

# COLLECT: all static files
python manage.py collectstatic --noinput
python manage.py wait_for_db    # Django Management Command 👉 APP_api > management > commands > wait_for_db.py

# RUN: uwsgi service
## --socket :#        run as TCP socket
## --workers          depends on mem / resources available -> 4 = "typical"
## --master           run as master service on terminal -> helps w/ graceful shutdown
## --enable-threads   multithreading
## --module           ⭐️ the application that uwsgi is going to run (4 = standard?)
uwsgi --socket :9000 --workers 4 --master --enable-threads --module DJANGO.wsgi