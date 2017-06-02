#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author: badpasta <beforget@hotmail.com> 
#
# Environment:
# Python power by version 2.7
#
# Create at: 2017-06-02 16:32:04

from mailclient import mail163


def main():
    the_mail = mail163()
    tp, data = the_mail.search()
    print data


if __name__ == '__main__':
    main()
