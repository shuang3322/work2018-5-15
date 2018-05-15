#!/usr/bin/python
# -*- coding: utf-8 -*-

'''基础需求：
让用户输入用户名密码
认证成功后显示欢迎信息
输错三次后退出程序

升级需求：
可以支持多个用户登录 (提示，通过列表存多个账户信息)
用户3次认证失败后，退出程序，再次启动程序尝试登录时，还是锁定状态（提示:需把用户锁定的状态存到文件里）'''

login_dir  = {'alex':'123123','admin':'123123'}
worry = []
cent = 0
while cent < 3:
    cent +=1
    name = str (input("name:").strip())
    password = str (input("password:").strip())
    if  login_dir.get(name) == password :
        if name in worry :
            print('Account Is Disabled;')
            return
        else:
            print('welcome')
            return
    else:
        print('worry:%s'%cent)
else:
    print("\033[0;31;40m worry to more exit system \033[0m")