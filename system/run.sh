#!/bin/sh

>&2 echo "Running migrations"
pipenv run python /srv/manage.py migrate

>&2 echo "Creating admin user"
pipenv run python /srv/manage.py create_admin_from_env

>&2 echo "Starting supervisor"
supervisord -c /srv/system/supervisord.conf
