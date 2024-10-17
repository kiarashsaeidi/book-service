#!/bin/sh

python manage.py migrate --no-input
python manage.py collectstatic --no-input

gunicorn book_service.wsgi:application --bind 0.0.0.0:5000