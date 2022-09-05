#!/bin/bash
yum update -y
yum install -y python3 python3-pip npm lsof
iptables -I INPUT -p tcp --dport 8000 -m conntrack --ctstate NEW,ESTABLISHED -j ACCEPT
iptables -I INPUT -p tcp --dport 80 -m conntrack --ctstate NEW,ESTABLISHED -j ACCEPT
# iptables -t nat -A OUTPUT -o lo -p tcp --dport 80 -j REDIRECT --to-port 8080
kill -9 $(lsof -t -i:8000)
kill -9 $(lsof -t -i:80)

python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.prod.txt

cd backend
python3 manage.py migrate
gunicorn blog.asgi:application -w 2 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000 --daemon

cd ../frontend
npm install
npm run build
nohup npm run preview -- --host 0.0.0.0 > nohup.out 2> nohup.err < /dev/null &