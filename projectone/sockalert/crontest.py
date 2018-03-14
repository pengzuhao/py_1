#!/usr/bin/python
# -*- coding:utf8 -*-

import os
import time


def ctbtest():
    data = open('ctb.log', 'a')
    string = str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))) + '\n'
    data.write(string)
    data.close()
    print (data)
    return data


if __name__ == '__main__':
    ctbtest()