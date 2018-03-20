#!/usr/bin/python
# -*- coding:utf8 -*-

import time
import requests
import os
from models import *
from sockmail import djmail
import logging
logger = logging.getLogger('django')
from projectone import settings


def ctbtest():
    try:
        newpath = settings.BASE_DIR
        data = open(os.path.join(newpath, 'projectone/logs/admin.log'), 'a')
        string = str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))) + '\n'
        data.write(string)
        data.close()
        return data
    except Exception as e:
        logging.error(e)


def getreqstatus():
    try:
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
                logger.error('Get MailUsers Failed!')
        for var in list_api:
            url = var.url
            data = var.data
            if len(data) > 1:
                r = requests.post(url, data)
                status = r.status_code
                if str(status).startswith('20') \
                    or str(status).startswith('30'):
                    pass
                else:
                    msg = '%s\'s status_code is %s for the first time' % (var.url, str(status))
                    logger.error(msg)
                    time.sleep(2)
                    r = requests.get(url)
                    status = r.status_code
                    if str(status).startswith('20') \
                            or str(status).startswith('30'):
                        pass
                    else:
                        msg = '%s\'s status_code is %s for the second time' % (var.url, str(status))
                        logger.error(msg)
                        time.sleep(2)
                        r = requests.get(url)
                        status = r.status_code
                        if str(status).startswith('20') \
                                or str(status).startswith('30'):
                            pass
                        else:
                            msg = '%s\'s status_code is %s for the third time' % (var.url, str(status))
                            logger.error(msg)
                            djmail(mailuserlist, msg)
            else:
                r = requests.get(url)
                status = r.status_code
                if str(status).startswith('20') \
                    or str(status).startswith('30'):
                    pass
                else:
                    msg = '%s\'s status_code is %s for the first time' % (var.url, str(status))
                    logger.error(msg)
                    time.sleep(2)
                    r = requests.get(url)
                    status = r.status_code
                    if str(status).startswith('20') \
                            or str(status).startswith('30'):
                        pass
                    else:
                        msg = '%s\'s status_code is %s for the second time' % (var.url, str(status))
                        logger.error(msg)
                        time.sleep(2)
                        r = requests.get(url)
                        status = r.status_code
                        if str(status).startswith('20') \
                                or str(status).startswith('30'):
                            pass
                        else:
                            msg = '%s\'s status_code is %s for the third time' % (var.url, str(status))
                            logger.error(msg)
                            djmail(mailuserlist, msg)
    except Exception as e:
        logger.error(e)


if __name__ == '__main__':
    ctbtest()
    getreqstatus()