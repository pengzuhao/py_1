#!/usr/bin/python
# coding:utf8
# 按顺序检测并启动tomcat

import sys
import os
import MySQLdb
import socket
import redis
import logging
import time

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='Restart.log',
                    filemode='a')


def start_iptables():
    try:
        os.system('service iptables restart')
    except Exception, e:
        logging.error(e)
        return False
    return True


def start_redis():
    try:
        os.system('service redis restart')
    except Exception, e:
        logging.error(e)
        return False
    return True


def conn_mysql(mysqlhost, mysqluser, mysqlpasswd, mysqlport, mysqldb):
    try:
        db = MySQLdb.connect(host=mysqlhost, user=mysqluser, passwd=mysqlpasswd, port=mysqlport, db=mysqldb, )
        cursor = db.cursor()
        sql = 'show tables;'
        cursor.execute(sql)
        result = cursor.fetchall()
        db.commit()
        num = len(result)
        if num > 0:
            return True
        else:
            return False
    except Exception, e:
        logging.error(e)
        return False


def conn_redis(redishost, redispassword, redisport, redisdb):
    try:
        r = redis.Redis(host=redishost,
                        password=redispassword,
                        port=redisport,
                        db=redisdb,
                        socket_connect_timeout=3,
                        socket_timeout=3)
        r.set('foo', 'bar')
        result = r.get('foo')
        if result == 'bar':
            return True
        else:
            logging.error('Get Key Failed')
            return False
    except Exception, e:
        logging.error(e)
        return False


def conn_redis_socket(redishost, redisport):
    s = socket.socket()
    s.settimeout(3)
    host = (redishost, redisport)
    try:
        s.connect(host)
    except socket.error, e:
        logging.error(e)
        return False
    return True


def start_tomcat(mysqlhost, mysqluser, mysqlpasswd, mysqlport, mysqldb,redishost,
                 redispassword, redisport, redisdb,
                 tomcatpath):
    try:
        flag = False
        for i in range(3):
            res_mysql = conn_mysql(mysqlhost, mysqluser, mysqlpasswd, mysqlport, mysqldb)
            res_redis = conn_redis(redishost, redispassword, redisport, redisdb)
            if res_mysql:
                if res_redis:
                    for item in tomcatpath_list:
                        os.system('source /etc/profile; %s/bin/startup.sh' % item)
                    flag = True
                    break
                else:
                    logging.error('redis not start')
            else:
                logging.error('mysql not start')
        if flag:
            print 'success'
            return True
        else:
            print 'failed'
            return False
    except Exception, e:
        logging.error(e)
        return False


if __name__ == "__main__":
    # start_iptables()
    # start_redis()
    mysqlhost = 'rm-bp14ba0hr97nd48s3o.mysql.rds.aliyuncs.com'
    mysqluser = 'penghao'
    mysqlpasswd = '5tgb^YHN'
    mysqlport = 3306
    mysqldb = 'qyyws'
    redishost = '172.17.21.13'
    redisport = 6379
    redispassword = '1qaz@WSX'
    redisdb = 0
    tomcatpath_list = ['/usr/local/src/apache-tomcat-a', '/usr/local/src/apache-tomcat-b']
    start_tomcat(mysqlhost, mysqluser, mysqlpasswd, mysqlport, mysqldb,
                 redishost, redispassword, redisport, redisdb,
                 tomcatpath_list)

