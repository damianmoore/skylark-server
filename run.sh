#!/bin/sh

>&2 echo "Running migrations"
python3 /srv/manage.py migrate

>&2 echo "Creating admin user"
python3 /srv/manage.py create_admin_from_env

>&2 echo "Starting supervisor"
supervisord -c /etc/supervisord.conf
