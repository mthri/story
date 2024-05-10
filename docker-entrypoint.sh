#!/bin/bash

# echo "Collecting static files..."
python3 manage.py collectstatic --noinput

# echo "Make migrations..."
python3 manage.py makemigrations --noinput

# echo "Migrate migrations to database..."
python3 manage.py migrate --noinpu

# set envs DJANGO_SUPERUSER_PASSWORD, DJANGO_SUPERUSER_USERNAME, DJANGO_SUPERUSER_EMAIL
# createsupseruser read these envs by default

if  [[ -n ${DJANGO_SUPERUSER_PASSWORD} ]] && \
    [[ -n ${DJANGO_SUPERUSER_USERNAME} ]] && \
    [[ -n ${DJANGO_SUPERUSER_EMAIL} ]]
then
    echo "Creating superuser..."
    python3 manage.py createsuperuser --noinput
else
    echo "DJANGO_SUPERUSER_[PASSWORD,USERNAME,EMAIL] does not provide, ignore creating supseruser..."
fi

# start server
gunicorn --bind 0.0.0.0:8000 config.wsgi:application