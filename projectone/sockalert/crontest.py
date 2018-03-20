#!/usr/bin/python
# -*- coding:utf8 -*-

import time
import requests
from models import *
from sockmail import djmail


def ctbtest():
    data = open('ctb.log', 'a')
    string = str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))) + '\n'
    data.write(string)
    data.close()
    return data


def getreqstatus():
    list_api = yx_api.objects.all()
    list_users = mailusers.objects.all()
    mailuserlist = []
    for var in list_users:
        muser = str(var.mail)
        userstatus = str(var.status)
        if userstatus == 'E':
            mailuserlist.append(muser)
        elif userstatus == 'D':
            pass
        else:
            print ('Get UserStatus Failed')
    for var in list_api:
        url = var.url
        data = var.data
        if len(data) > 1:
            r = requests.post(url, data)
            status = r.status_code
            if str(status).startswith('20') \
                and str(status).startswith('30'):
                pass
            else:
                pass
        else:
            r = requests.get(url)
            status = r.status_code
            if str(status).startswith('20') \
                and str(status).startswith('30'):
                pass
            else:
                pass


if __name__ == '__main__':
    ctbtest()
    getreqstatus()