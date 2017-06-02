#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author: badpasta <beforget@hotmail.com> 
#
# Environment:
# Python power by version 2.7
#
# Create at: 2017-06-02 16:33:43

from smtplib import SMTP
from imaplib import IMAP4
from contextlib import contextmanager


class mailClientBase(object):
    def __init__(self):
        pass

    @property
    def recvclient(self):
        return IMAP4(self.recvserver, self.recvport)

    @property
    def recvlogin(self):
        recv = self.recvclient
        recv.login(self.user, self.passwd)
        return recv

    @contextmanager
    def select(self):
        try:
            client = self.recvlogin
            client.select()
            yield client
        except Exception, e:
            print e
            raise
        finally:
            client.close()
            client.logout()

    def search(self, *keyword):
        with self.select() as recv:
            recv_type, (recv_data, ) = recv.search(None, 'ALL')

        return recv_type, recv_data


class mail163(mailClientBase):
    user = '882406701'
    passwd = 'whereareyou@y'
    sendserver =  'smtp.163.com'
    sendport = 25
    recvserver = 'imap.163.com'
    recvport = 143



















