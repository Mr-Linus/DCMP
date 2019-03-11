#!/usr/bin/env bash
cd /DCMP/DCMP && celery -A DCMP worker -l info &
uwsgi --ini /DCMP/DCMP_uwsgi.ini
