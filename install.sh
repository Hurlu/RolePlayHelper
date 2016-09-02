#!/bin/bash
sudo pacman -S python-virtualenv sqlite || sudo apt-get install virtualenv sqlite3
virtualenv ./.rp_virtualenv
source ./.rp_virtualenv/bin/activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate