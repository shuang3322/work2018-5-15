#!/usr/bin/python
# -*- coding: utf-8 -*-
def NO1_test():
    li=['alex', 'eric', 'rain']
    print('NO1_test :',"_".join(li))


def NO2_test():
    li = ["alec", " aric", "Alex", "Tony", "rain"]
    tu = ("alec", " aric", "Alex", "Tony", "rain")
    dic = {'k1': "alex", 'k2': ' aric', "k3": "Alex", "k4": "Tony"}
    for item in li:
        item = item.strip()
        if  item[0] == 'a' or item [0] == 'A':
            if item[-1] == 'c':
                print('NO2_test_li:',item)
    for item in tu:
        item = item.strip()
        if item[0] == 'a' or item[0] == 'A':
            if item[-1] == 'c':
                print('NO2_test_tu:', item)
    for key,item in dic.items():
        item = item.strip()
        if item[0] == 'a' or item[0] == 'A':
            if item[-1] == 'c':
                print('NO2_test_dic:', item)
def NO3_test():
    li=['alex', 'eric', 'rain']
    li.append('seven')
    print("1——",li)
    li.insert(0,'Tony')
    print("2——",li)
    li[1]='Kelly'
    print("3——",li)
    li.remove("eric")
    print("4——",li)
    print("5——", li[1])
    li.pop(1)
    print("5——", li)
    li.pop(2)
    print("5——", li)

def No4_test():
    li = ["hello", 'seven', ["mon", ["h", "kelly"], 'all'], 123, 446]
    print(li[2][1][1])
    li[2][2]='ALL'
    print(li)

def No5_test():
    tu=('alex', 'eric', 'rain')
    print(len(tu))
    print(tu[1])
    print(tu[0:2])
    for item in tu:
        print(item)
    for item in range(len(tu)):
        print(item,tu[item])
    for key,item in enumerate(tu,100):
        print(key,item)
def No6_test():
    tu = ("alex", [11, 22, {"k1": 'v1', "k2": ["age", "name"], "k3": (11, 22, 33)}, 44])
def No7_test():
    dic = {'k1': "v1", "k2": "v2", "k3": [11, 22, 33]}
    for key,item in dic.items():
        print(key)
        print(item)
        print(key,item)
    dic['k4']='v4'
    print(dic)
    dic['k1']= 'alex'
    print(dic)
    dic['k3'].append(44)
    print(dic)
    dic['k3'].insert(0,18)
    print(dic)
def No8_test():
    s = "alex"
    l_s = list(s)
    print(l_s)
    t_s = tuple(s)
    print(t_s)
    li = ["alex", "seven"]
    t_li = tuple(li)
    print(t_li)
    tu = ('Alex', "seven")
    l_tu = list(tu)
    print(l_tu)
    dic_li = {}
    for key in range(10,12):
        dic_li[key] = li[key-10]
    print(dic_li)
def No9_test():
    ls= [11, 22, 33, 44, 55, 66, 77, 88, 99, 90]
    dir =  {'k1':[],'k2':[]}
    for item in ls:
        if  int(item) >66:
            dir['k1'].append(item)
        else:
            dir['k2'].append(item)
    print(dir)
def No10_test():

    li = ["手机", "电脑", '鼠标垫', '游艇']

    while True:
        in_id = input("1:添加商品 2：显示所有商品").strip()
        if in_id == '2':
            for index,item in enumerate(li,1):
                print(index,item)
        elif in_id == '1':
            in_item = input("添加商品:").strip()
            li.append(in_item)
            print(li)
        else:
            continue

def No13_test():
    l1 = [11, 22, 33]
    l2 = [22, 33, 44]
    l1_set = set(l1)
    l2_set = set(l2)
    a = l1_set|l2_set
    b = l1_set&l2_set
    c = l1_set-l2_set
    d = l1_set^l2_set
    print(a,b,c,d)
def No14_test():
    for item in range(1,101):
        print(item)
    for item in range(1,100):
        print(100-item)
    i =1
    while i <=100:
        print(i)
        i+=1
    i2 = 100
    while i2 >= 1:
        print(i2)
def work2():
    menu = {
        '北京': {
            '海淀': {
                '五道口': {
                    'soho': {},
                    '网易': {},
                    'google': {}
                },
                '中关村': {
                    '爱奇艺': {},
                    '汽车之家': {},
                    'youku': {},
                },
                '上地': {
                    '百度': {},
                },
            },
            '昌平': {
                '沙河': {
                    '老男孩': {},
                    '北航': {},
                },
                '天通苑': {},
                '回龙观': {},
            },
            '朝阳': {},
            '东城': {},
        },
        '上海': {
            '闵行': {
                "人民广场": {
                    '炸鸡店': {}
                }
            },
            '闸北': {
                '火车战': {
                    '携程': {}
                }
            },
            '浦东': {},
        },
        '山东': {},
    }
    exit_flag = False
    current_layer = menu

    layers = [menu]
    while not  exit_flag:
        for k in current_layer:
            print(k,type(k))
        choice = input(">>:").strip()
        if choice == "b" or choice == "B":
            if menu == layers[-1] :
                current_layer = menu
                layers = [menu]
            else:
                current_layer = layers[-1]
                layers.pop()
        elif choice == "q" or choice == "Q":
            exit_flag = True
            continue
        elif choice not  in current_layer:continue
        else:
            layers.append(current_layer)
            current_layer = current_layer.get(choice)
def work3():
    goods = [
    {"name": "电脑", "price": 1999},
    {"name": "鼠标", "price": 10},
    {"name": "游艇", "price": 20},
    {"name": "美女", "price": 998}]
    wage_balance = input("输入工资额度：").strip()
    wage_balance = int(wage_balance)
    go = True
    pay_item =[]
    while go ==True:
        for key,item in enumerate(goods):
            print(key,item.get('name'),item.get('price'))
        print("q：退出")
        choice_item_id  = input("购买商品序号： ").strip()
        if  choice_item_id == 'q':
            go = False
            for item in pay_item:
                print("\033[0;33;40m %s \033[0m"%(item))
        else:
            try:
                choice_item_id = int(choice_item_id)
                choice_item_price = goods[choice_item_id].get('price')
                choice_item_name = goods[choice_item_id].get('name')
                if wage_balance >= choice_item_price:
                    wage_balance = wage_balance - choice_item_price
                    pay_item.append(choice_item_name)
                    print("加入商品\033[0;35;40m %s \033[0m" % (choice_item_name))
                else:
                    print("余额不足,现有余额：\033[0;31;40m %s \033[0m"%(wage_balance))
            except Exception as e :
                print("输入错误")
'''基础需求：
让用户输入用户名密码
认证成功后显示欢迎信息
输错三次后退出程序

升级需求：
可以支持多个用户登录 (提示，通过列表存多个账户信息)
用户3次认证失败后，退出程序，再次启动程序尝试登录时，还是锁定状态（提示:需把用户锁定的状态存到文件里）'''

def work1():
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
work1()

