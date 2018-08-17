#!/bin/bash
python DCMP/manage.py runserver 0.0.0.0:8000 &
celery -A DCMP worker -l info