#!/usr/bin/python
# coding:utf8

import time
import MySQLdb

def a():
    flag = False
    for i in range(5):
        if i == 1:
            flag = True
            break
        time.sleep(2)
    print flag


if __name__ == '__main__':
    pass