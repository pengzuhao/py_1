#!/usr/bin/python
# -*- coding:utf8 -*-

from binascii import a2b_hex, b2a_hex
from Crypto.Cipher import AES


class crypts():
    def __init__(self):
        self.mode = AES.MODE_CBC
        self.length = 16

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

    def encrypt(self, keyone, keytwo, string):
        ins = crypts()
        ca = AES.new(keyone, self.mode, keytwo)
        post = ca.encrypt(ins.exchangeencrypt(string))
        b_post = b2a_hex(post)
        return b_post

    def decrypt(self, keyone, keytwo, string):
        ca = AES.new(keyone, self.mode, keytwo)
        pre = ca.decrypt(a2b_hex(string))
        a_pre = pre.rstrip('\0')
        return a_pre


if __name__ == '__main__':
    keyone = 'aaaaaaaaaaaaaaaa'
    keytwo = b'0000000000000000'
    string = 'sockdb'
    ins = crypts()
    print (ins.encrypt(keyone, keytwo, string))
    enstr = 'e35f18f432f2e0fb849eaf59b5c5d272'
    print (ins.decrypt(keyone, keytwo, enstr))