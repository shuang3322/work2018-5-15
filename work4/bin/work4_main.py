#!/usr/bin/env python
# -*- coding:utf-8 -*
import os
import sys
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(base_dir)
sys.path.append(base_dir)
from core import work4
if __name__ == '__main__':
    work4.main()