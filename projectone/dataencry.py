#!/usr/bin/python
# -*- coding:utf8 -*-

import os
from binascii import a2b_hex, b2a_hex
from Crypto.Cipher import AES


class crypts():
    def __init__(self):
        self.mode = AES.MODE_CBC
        self.length = 16
        self.keyone = os.environ.get('keyone')
        self.keytwo = os.environ.get('keytwo')

    def exchangeencrypt(self, string):
        count = len(string)
        if count < self.length:
            mis = self.length - count
            text = string + ('\0' * mis)
            return text
        elif count > self.length:
            mis = self.length - (count % self.length)
            text = string + ('\0' * mis)
            return text
        else:
            text = string
            return text

    def encrypt(self, string):
        ins = crypts()
        ca = AES.new(self.keyone, self.mode, self.keytwo)
        post = ca.encrypt(ins.exchangeencrypt(string))
        b_post = b2a_hex(post)
        return b_post

    def decrypt(self, string):
        ca = AES.new(self.keyone, self.mode, self.keytwo)
        pre = ca.decrypt(a2b_hex(string))
        a_pre = pre.rstrip('\0')
        return a_pre


if __name__ == '__main__':
    pass