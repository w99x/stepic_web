#!/bin/bash
etcdir=/home/box/etc
gunicorn  ask.wsgi:application -c $etcdir/gunicorn.py