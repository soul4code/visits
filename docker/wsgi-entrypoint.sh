#!/bin/sh

set -e

. /app/.venv/bin/activate

until cd .
do
    echo "Waiting for server volume..."
done

until $HOME/.poetry/bin/poetry run python manage.py migrate
do
    echo "Waiting for db to be ready..."
    sleep 2
done

$HOME/.poetry/bin/poetry run python manage.py defaultuser_create
$HOME/.poetry/bin/poetry run python manage.py collectstatic --noinput
# TODO set superuser!
gunicorn visits.wsgi --bind 0.0.0.0:8000 --workers 4 --threads 4 --reload
#./manage.py runserver 0.0.0.0:8003