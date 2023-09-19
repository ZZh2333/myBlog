#!/bin/bash
set -e
cd ~/myblog && echo "Autoupdate starting......"
echo "Now in `pwd`"
source /root/anaconda3/bin/activate class_BigData || echo "error source!!!"
uwsgi --stop uwsgi.pid
git pull -f origin main
uwsgi uwsgi.ini && echo "success!" || echo "failed!!!!!!!!"