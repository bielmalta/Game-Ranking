#!/bin/bash
set -o errexit

echo "Running Django migrations..."
python manage.py migrate --noinput

echo "Ensuring superuser (reads DJANGO_SUPERUSER_* env vars; skipped if unset)..."
python manage.py ensure_superuser

echo "Starting gunicorn..."
gunicorn Game_Ranking.wsgi:application --bind 0.0.0.0:8000
