#!/usr/bin/python
# -*- coding: utf-8 -*-

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