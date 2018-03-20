#!/usr/bin/python
# --*-- coding:utf8 --*--

import os
from dataencry import crypts
from django.core.mail import send_mail, send_mass_mail


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