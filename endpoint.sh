#!/bin/bash
python DCMP/manage.py runserver 0.0.0.0:8000 &
cd DCMP && celery -A DCMP worker -l info