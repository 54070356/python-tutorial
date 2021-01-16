#!/usr/bin/env bash

if [ -z "${UWSGI_PROCESSES}" ];then
	UWSGI_PROCESSES=1
fi
echo UWSGI_PROCESSES=$UWSGI_PROCESSES

if [ -z "$UWSGI_THREADS" ];then
	UWSGI_THREADS=1
fi
echo UWSGI_THREADS=$UWSGI_THREADS

if [ -z "$PORT" ];then
	PORT=10000
fi
echo PORT=$PORT

uwsgi --http-socket :${PORT} --enable-threads --threads=${UWSGI_THREADS} --processes=${UWSGI_PROCESSES} --wsgi-file service.py --buffer-size 32768 --chmod-socket=666 --gevent-monkey-patch --disable-logging --callable app
