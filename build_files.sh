#!/bin/bash
python -m pip install -r requirements.txt --break-system-packages
python manage.py collectstatic --noinput --clear
