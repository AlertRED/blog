#!/bin/bash

yum update
yum install -y python3 python3-pip
iptables -I INPUT -p tcp --dport 8000 -m conntrack --ctstate NEW,ESTABLISHED -j ACCEPT
iptables -I INPUT -p tcp --dport 4173 -m conntrack --ctstate NEW,ESTABLISHED -j ACCEPT
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements
pip3 install gunicorn uvicorn

cd backend
python3 manage.py migrate
nohup gunicorn blog.asgi:application -w 2 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000

cd ../frontend
npm install
npm run build
nohup npm run preview -- --host 0.0.0.0

return