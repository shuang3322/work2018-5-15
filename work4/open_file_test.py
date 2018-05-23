#!/usr/bin/env python
# -*- coding:utf-8 -*
import os
import sys
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(base_dir)
with open('db/name.db','r',encoding='utf-8') as f:
    f1= f.readlines()
    for item in f1 :
        print(item.split(",")[0:])

ss = "aaa"
ss.strip()