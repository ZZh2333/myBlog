#!/bin/bash
cd ~/myblog && echo "Autoupdate starting......" || exit 1
echo "Now in `pwd`"
source /root/anaconda3/bin/activate class_BigData || echo "error source!!!"
uwsgi --stop uwsgi.pid
git pull -f origin main
chmod u+x update.sh
uwsgi uwsgi.ini && echo "success!" || echo "failed!!!!!!!!"