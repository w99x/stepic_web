#!/bin/bash
mkdir --parents /home/box/web/public/img
mkdir --parents /home/box/web/public/css
mkdir --parents /home/box/web/public/js
mkdir --parents /home/box/web/uploads
mkdir --parents /home/box/web/etc

cp -rf ./nginx.conf /home/box/web/etc/
sudo mkdir --parents /etc/nginx/sites-enabled/default
sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
