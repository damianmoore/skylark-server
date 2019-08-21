#!/bin/sh
if [ "$ENV" = "dev" ]
then
  >&2 echo "Starting Django runserver as in dev mode"
  cd /srv && DJANGO_SETTINGS_MODULE=skylark.settings pipenv run python /srv/manage.py runserver 0.0.0.0:8000
else
  >&2 echo "Starting Gunicorn server as in prd/stg mode"
  cd /srv && pipenv run gunicorn -b 0.0.0.0:8000 -w 4 skylark.wsgi:application
fi
