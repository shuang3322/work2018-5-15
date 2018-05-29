#!/usr/bin/env python
# -*- coding:utf-8 -*


def print_log(msg, msg_type='info'):
    if msg_type == 'error':
        print("\033[31;1mError:%s\033[0m" % msg)
    else:
        print("\033[32;1mInfo:%s\033[0m" % msg)
