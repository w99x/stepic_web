#!/bin/bash
webdir=/home/box/web
etcdir=/home/box/etc
mkdir --parents $webdir
mkdir --parents $etcdir

cp -rf ./gunicorn_conf.py $etcdir/gunicorn.py
cp -rf ./nginx.conf $etcdir/
cp -rf ./ask $webdir/ask

sudo ln -sf $etcdir/gunicorn.py  /etc/gunicorn.d/gunicorn.py
sudo ln -sf $etcdir/nginx.conf /etc/nginx/sites-enabled/default

sudo /etc/init.d/nginx restart
sudo /etc/init.d/mysql restart
