#!/bin/bash

set -e

if [ "$2" == 'beat' ]; then
  exec celery beat -A django_docker -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler
fi

if [ "$2" == 'worker' ]; then
  exec celery -A django_docker worker -l INFO -P gevent
fi

if [ "$2" == 'web' ]; then
    exec gunicorn django_docker.wsgi -b 0.0.0.0:9000 --workers 4 --worker-class gthread --threads 20 --timeout 60
fi

if [ "$2" == 'migrate' ]; then
    exec python manage.py migrate
fi
