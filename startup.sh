#!/bin/bash
echo "Running Django migrations..."
python manage.py migrate --noinput
echo "Starting gunicorn..."
gunicorn Game_Ranking.wsgi:application --bind 0.0.0.0:8000
