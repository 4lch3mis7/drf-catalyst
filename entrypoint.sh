#!/usr/bin/bash

source .venv/bin/activate

python3 manage.py migrate
python3 manage.py collectstatic --no-input
python3 manage.py createsuperuser --no-input
python3 -m celery -A drf_catalyst worker -l info -B -D

exec "$@"
