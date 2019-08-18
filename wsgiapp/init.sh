#!/bin/bash
mkdir --parents /home/box/web
mkdir --parents /home/box/etc

cp -rf ./hello_app.py /home/box/web/hello.py
cp -rf ./hello_conf.py /home/box/web/etc/hello.py
cp -rf ./nginx.conf /home/box/web/etc/

sudo ln -sf /home/box/web/etc/hello.py  /etc/gunicorn.d/hello.py
sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default

