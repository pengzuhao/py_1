#!/bin/bash

list=$(ps axu|grep -vE "grep|$0" |grep manage.py|awk '{print $2}')
for i in $list
do
    for j in a,b
    do
    kill -9 $i &>/dev/null
    sleep 1
    done
done
sleep 1
nohup /usr/bin/python manage.py runserver 0.0.0.0:80 &

