#!/usr/bin/python
# -*- coding:utf8 -*-

import os
import time
import requests
from models import *
from django.core.mail import send_mail, send_mass_mail
from dataencry import crypts


def djmail(userlist, msg):
    ins = crypts()
    bstr = os.environ.get('mailfromuser')
    mailfromuser = ins.decrypt(bstr)
    send_mail(
        u'益杏业务接口报警',
        msg,
        mailfromuser,
        userlist,
        fail_silently=False,
    )


def ctbtest():
    data = open('ctb.log', 'a')
    string = str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))) + '\n'
    data.write(string)
    data.close()
    return data


def getreqstatus():
    list_api = yx_api.objects.all()
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