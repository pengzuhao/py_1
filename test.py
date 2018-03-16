#!/usr/bin/python
# -*- coding:utf8 -*-


import requests, os


def a():
    url = 'https://hms.yixinghealth.com/web/his/index.htm'
    r = requests.get(url)
    status = r.status_code
    print (status)


def b():
    url = 'https://hms.yixinghealth.com/yixing_api/qygl/xt_ygxxb_add?t=1521184120586&openid=haoliji&token=c379717160b25b4cf2be921e9b066d994fb670f4?yggh=125&ygxm=萧珊&ygxb=2&csrq=&sfzh=410501199001019848&ygzw=总账会计&rzsj=2017-08-10&lxfs=13788175563&jtdz=上海浦东新区石头子路32号&bmxxid=f95efa607f674c70a60fdc52d64cb8cb&ygxxid=e9a16e9d04644da7a2732e6bb78517e4&txtp=&ygxs=0&gwxxid='
    data = '{}'
    r = requests.post(url, data)
    text = r.text
    status = r.status_code
    if str(status).startswith('40'):
        print (status)
    else:
        print ('wrong')


def mailtest():
    from sockalert.crontest import djmail
    userlist = ['zuhao.peng@aliyun.com']
    msg = 'this is a test '
    djmail(userlist, msg)


if __name__ == '__main__':
    pass