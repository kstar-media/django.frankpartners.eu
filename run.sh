#!/bin/bash

cd /var/www/django.frankpartners.eu
apt install python3.8-venv

python -m pip install virtualenv
python -m venv venv
source venv/bin/activate

pip install -r requirements.txt

cd /var/www/django.frankpartners.eu/web
python ./manage.py runserver 0.0.0.0:81