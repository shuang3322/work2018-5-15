#!/usr/bin/env python
# -*- coding:utf-8 -*
with open('name.db','r',encoding='utf-8') as f:
    f1= f.readlines()
    print(f1,type(f1))

ss = "aaa"
ss.strip()