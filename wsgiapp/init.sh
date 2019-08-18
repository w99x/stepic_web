#!/bin/bash
webdir=/home/box/web
etcdir=/home/box/etc
mkdir --parents $webdir
mkdir --parents $etcdir

cp -rf ./hello_app.py $webdir/hello.py
cp -rf ./hello_conf.py $etcdir/hello.py
cp -rf ./nginx.conf $etcdir/

sudo ln -sf $etcdir/hello.py  /etc/gunicorn.d/hello.py
sudo ln -sf $etcdir/nginx.conf /etc/nginx/sites-enabled/default/nginx.conf

